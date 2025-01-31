from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg


class MovieList(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_path = models.URLField()
    release_date = models.DateField()
    runtime = models.IntegerField(null=True, blank=True)
    
    def average_rating(self):
        avg_rating = self.moviereview_set.aggregate(Avg('rating'))['rating__avg']
        if avg_rating is not None:
            return round(avg_rating, 1)
        return None

    def __str__(self):
        return f"{self.title} | {self.release_date}"


class SeriesList(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_path = models.URLField()
    first_air_date = models.DateField()
    last_air_date = models.DateField(null=True, blank=True)
    number_of_seasons = models.IntegerField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.title


class Season(models.Model):
    series = models.ForeignKey(SeriesList, on_delete=models.CASCADE)
    season_number = models.IntegerField()
    episode_count = models.IntegerField()
    description = models.TextField()
    first_air_date = models.DateField()
    last_air_date = models.DateField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.series.title} | Season {self.season_number}"


class MovieReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(MovieList, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['date_created']

    def __str__(self):
        return f"Review by {self.user.username} on {self.movie.title}"


class SeriesReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    series = models.ForeignKey(SeriesList, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Review by {self.user.username} on {self.series.title}"


class SeasonReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"Review by {self.user.username} on {self.season.series.title} | "
            f"Season {self.season.season_number}"
        )


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MovieGenre(models.Model):
    movie = models.ForeignKey(MovieList, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class SeriesGenre(models.Model):
    series = models.ForeignKey(SeriesList, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)


class ReviewEntity(models.Model):
    CONTENT_TYPE_CHOICES = [
        ('movie_review', 'Movie Review'),
        ('series_review', 'Series Review'),
        ('season_review', 'Season Review'),
    ]
    content_type = models.CharField(
        max_length=20, choices=CONTENT_TYPE_CHOICES
    )
    review_id = models.IntegerField()


class ReviewLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_entity = models.ForeignKey(ReviewEntity, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)


class ReviewComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_entity = models.ForeignKey(ReviewEntity, on_delete=models.CASCADE)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
