import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")


def fetch_movies(page=1):
    """Fetch popular movies from TMDb."""
    url = (
        f"https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}"
        f"&language=en-US&page={page}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_movie_details(tmdb_id):
    """Fetch movie details from TMDb."""
    url = (
        f"https://api.themoviedb.org/3/movie/{tmdb_id}?api_key={API_KEY}"
        f"&language=en-US"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_tv_series(page=1):
    """Fetch popular TV series from TMDb."""
    url = (
        f"https://api.themoviedb.org/3/tv/popular?api_key={API_KEY}"
        f"&language=en-US&page={page}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_tv_series_details(tmdb_id):
    """Fetch TV series details from TMDb."""
    url = (
        f"https://api.themoviedb.org/3/tv/{tmdb_id}?api_key={API_KEY}"
        f"&language=en-US"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
