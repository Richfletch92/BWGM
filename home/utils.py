import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get API key and base URL from environment variables
API_KEY = os.getenv("TMDB_API_KEY")
BASE_URL = os.getenv("TMDB_BASE_URL")


def fetch_movies(page=1, language='en-US'):
    """
    Fetch popular movies from TMDb with original language set to English.

    Args:
        page (int): The page number for pagination (default is 1).
        language (str): The language code for the movie titles (default is
                        'en-US').

    Returns:
        dict: A JSON response containing movie data if successful, None
              otherwise.
    """
    url = (
        f"{BASE_URL}/discover/movie?api_key={API_KEY}"
        f"&language={language}&page={page}"
        f"&with_original_language=en"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_movie_details(tmdb_id):
    """
    Fetch detailed information about a specific movie from TMDb.

    Args:
        tmdb_id (int): The TMDb ID of the movie.

    Returns:
        dict: A JSON response containing movie details if successful, None
              otherwise.
    """
    url = (
        f"{BASE_URL}/movie/{tmdb_id}?api_key={API_KEY}"
        f"&language=en-US"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_tv_series(page=1, language='en-US'):
    """
    Fetch popular TV series from TMDb with original language set to English.

    Args:
        page (int): The page number for pagination (default is 1).
        language (str): The language code for the TV series titles (default is
                        'en-US').

    Returns:
        dict: A JSON response containing TV series data if successful, None
              otherwise.
    """
    url = (
        f"{BASE_URL}/discover/tv?api_key={API_KEY}"
        f"&language={language}&page={page}"
        f"&with_original_language=en"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_tv_series_details(tmdb_id):
    """
    Fetch detailed information about a specific TV series from TMDb.

    Args:
        tmdb_id (int): The TMDb ID of the TV series.

    Returns:
        dict: A JSON response containing TV series details if successful, None
              otherwise.
    """
    url = (
        f"{BASE_URL}/tv/{tmdb_id}?api_key={API_KEY}"
        f"&language=en-US"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_season_details(tmdb_id, season_number):
    """
    Fetch detailed information about a specific season of a TV series from
    TMDb.

    Args:
        tmdb_id (int): The TMDb ID of the TV series.
        season_number (int): The season number of the series.

    Returns:
        dict: A JSON response containing season details if successful, None
              otherwise.
    """
    url = (
        f"{BASE_URL}/tv/{tmdb_id}/season/{season_number}?api_key={API_KEY}"
        f"&language=en-US"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None


def fetch_genres():
    """
    Fetch the list of movie genres from TMDb.

    Returns:
        dict: A JSON response containing genre data if successful, None
              otherwise.
    """
    url = (
        f"{BASE_URL}/genre/movie/list?api_key={API_KEY}"
        f"&language=en-US"
    )
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None
