import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = os.getenv("TMDB_BASE_URL")


def fetch_movies(page=1):
    """Fetch popular movies from TMDb."""
    url = (
        f"{BASE_URL}/movie/popular?api_key={API_KEY}"
        f"&language=en-US&page={page}"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_movie_details(tmdb_id):
    """Fetch movie details from TMDb."""
    url = (
        f"{BASE_URL}/movie/{tmdb_id}?api_key={API_KEY}"
        f"&language=en-US"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_tv_series(page=1, language='en-US'):
    """Fetch popular TV series from TMDb with original language set to English."""
    url = (
        f"{BASE_URL}/discover/tv?api_key={API_KEY}"
        f"&language={language}&page={page}&with_original_language=en"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_tv_series_details(tmdb_id):
    """Fetch TV series details from TMDb."""
    url = (
        f"{BASE_URL}/tv/{tmdb_id}?api_key={API_KEY}"
        f"&language=en-US"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
