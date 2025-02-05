# movies/management/commands/fetch_data.py
from django.core.management.base import BaseCommand
from home.utils import (
    fetch_movies,
    fetch_movie_details,
    fetch_tv_series,
    fetch_tv_series_details,
    fetch_season_details,
    fetch_genres
)
from home.models import (
    MovieList, SeriesList, SeasonList, Genre, MovieGenre, SeriesGenre
)


class Command(BaseCommand):
    help = (
        "Fetch movies and TV series from TMDb and store detailed information"
    )

    def handle(self, *args, **kwargs):
        # Fetch genres
        genre_data = fetch_genres()
        if genre_data:
            for genre in genre_data['genres']:
                Genre.objects.update_or_create(
                    id=genre['id'],
                    defaults={'name': genre['name']}
                )
        self.stdout.write(
            self.style.SUCCESS('Genres fetched and stored successfully!')
        )

        # Fetch popular movies
        for page in range(1, 6):  # Fetch first 5 pages of popular movies
            data = fetch_movies(page)
            if data:
                for movie_data in data['results']:
                    tmdb_id = movie_data['id']
                    # Fetch detailed data
                    details = fetch_movie_details(tmdb_id)
                    if details:
                        movie, created = MovieList.objects.update_or_create(
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
                        # Fetch and store genres
                        for genre in details['genres']:
                            genre_obj, _ = Genre.objects.get_or_create(
                                id=genre['id'],
                                defaults={'name': genre['name']}
                            )
                            MovieGenre.objects.update_or_create(
                                movie=movie,
                                genre=genre_obj
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
                        series, created = SeriesList.objects.update_or_create(
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
                        # Fetch and store genres
                        for genre in details['genres']:
                            genre_obj, _ = Genre.objects.get_or_create(
                                id=genre['id'],
                                defaults={'name': genre['name']}
                            )
                            SeriesGenre.objects.update_or_create(
                                series=series,
                                genre=genre_obj
                            )
                        # Fetch and store season details
                        for season_number in range(
                            1, series.number_of_seasons + 1
                        ):
                            season_details = fetch_season_details(
                                tmdb_id, season_number
                            )
                            if season_details:
                                first_air_date = season_details.get(
                                    'air_date', None
                                )
                                if not first_air_date and season_details[
                                    'episodes'
                                ]:
                                    first_air_date = season_details[
                                        'episodes'
                                    ][0].get('air_date', None)
                                if first_air_date:
                                    SeasonList.objects.update_or_create(
                                        series=series,
                                        season_number=season_number,
                                        defaults={
                                            'episode_count': len(
                                                season_details['episodes']
                                            ),
                                            'description': season_details[
                                                'overview'
                                            ],
                                            'first_air_date': first_air_date,
                                            'last_air_date': season_details.get(
                                                'air_date', None
                                            ),
                                            'poster_path': (
                                                f"https://image.tmdb.org/t/p/w500"
                                                f"{season_details['poster_path']}"
                                            ),
                                        }
                                    )
        self.stdout.write(
            self.style.SUCCESS('TV series and seasons fetched and stored successfully!')
        )
