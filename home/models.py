from django.db import models

# Create your models here.
class Movie(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    poster_path = models.URLField()
    release_date = models.DateField()
    runtime = models.IntegerField(null=True, blank=True)  # Add runtime here

    def __str__(self):
        return f"{self.title} | {self.release_date}"