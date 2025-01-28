# movies/management/commands/fetch_data.py
from django.core.management.base import BaseCommand
from home.utils import (
    fetch_movies,
    fetch_movie_details,
    fetch_tv_series,
    fetch_tv_series_details
)
from home.models import MovieList, SeriesList


class Command(BaseCommand):
    help = (
        "Fetch movies and TV series from TMDb and store detailed information"
    )

    def handle(self, *args, **kwargs):
        # Fetch popular movies
        for page in range(1, 6):  # Fetch first 5 pages of popular movies
            data = fetch_movies(page)
            if data:
                for movie_data in data['results']:
                    tmdb_id = movie_data['id']
                    # Fetch detailed data
                    details = fetch_movie_details(tmdb_id)
                    if details:
                        MovieList.objects.update_or_create(
                            tmdb_id=tmdb_id,
                            defaults={
                                'title': details['title'],
                                'description': details['overview'],
                                'poster_path': (
                                    f"https://image.tmdb.org/t/p/w500"
                                    f"{details['poster_path']}"
                                ),
                                'release_date': details['release_date'],
                                # Get runtime if available
                                'runtime': details.get('runtime', None),
                            }
                        )
        self.stdout.write(
            self.style.SUCCESS('Movies fetched and stored successfully!')
        )

        # Fetch popular TV series
        for page in range(1, 6):  # Fetch first 5 pages of popular TV series
            data = fetch_tv_series(page)
            if data:
                for series_data in data['results']:
                    tmdb_id = series_data['id']
                    # Fetch detailed data
                    details = fetch_tv_series_details(tmdb_id)
                    if details:
                        SeriesList.objects.update_or_create(
                            tmdb_id=tmdb_id,
                            defaults={
                                'title': details['name'],
                                'description': details['overview'],
                                'poster_path': (
                                    f"https://image.tmdb.org/t/p/w500"
                                    f"{details['poster_path']}"
                                ),
                                'first_air_date': details['first_air_date'],
                                'last_air_date': details.get(
                                    'last_air_date', None
                                ),
                                'number_of_seasons': details.get(
                                    'number_of_seasons', None
                                ),
                            }
                        )
        self.stdout.write(
            self.style.SUCCESS('TV series fetched and stored successfully!')
        )
