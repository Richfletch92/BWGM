# movies/management/commands/fetch_data.py
from django.core.management.base import BaseCommand
from home.utils import fetch_movies, fetch_movie_details
from home.models import Movie

class Command(BaseCommand):
    help = "Fetch movies from TMDb and store detailed information"

    def handle(self, *args, **kwargs):
        # Fetch popular movies
        for page in range(1, 6):  # Fetch first 5 pages of popular movies
            data = fetch_movies(page)
            if data:
                for movie_data in data['results']:
                    tmdb_id = movie_data['id']
                    details = fetch_movie_details(tmdb_id)  # Fetch detailed data
                    if details:
                        Movie.objects.update_or_create(
                            tmdb_id=tmdb_id,
                            defaults={
                                'title': details['title'],
                                'description': details['overview'],
                                'poster_path': f"https://image.tmdb.org/t/p/w500{details['poster_path']}",
                                'release_date': details['release_date'],
                                'runtime': details.get('runtime', None),  # Get runtime if available
                            }
                        )
        self.stdout.write(self.style.SUCCESS('Movies fetched and stored successfully!'))
