from django.db import models


# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_path = models.URLField()
    release_date = models.DateField()
    runtime = models.IntegerField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} | {self.release_date}"


# Add Series model here 
class Series(models.Model):
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


# class Season(models.Model):
#     series_id = models.ForeignKey(Series, on_delete=models.CASCADE)
#     season_number = models.IntegerField()
#     episode_count = models.IntegerField()
#     desciption = models.TextField()
#     air_date = models.DateField()
    
#     def __str__(self):
#         return f"{self.series.title} | Season {self.season_number}"
