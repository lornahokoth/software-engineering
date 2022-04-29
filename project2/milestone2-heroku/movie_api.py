"""movie_api.py does all the heavy lifting for pulling data
from the various APIs"""
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/"
TMDB_KEY = os.getenv("TMDB_KEY")
MOVIES = ["550988", "635302", "634649"]


def get_movie_titles():
    """Function to call TMDB to get the movie titles for the ids provided in MOVIES"""
    params = {"api_key": TMDB_KEY}
    movie_titles = []
    for movie_id in MOVIES:
        url = BASE_URL + "movie/" + movie_id
        response = requests.get(url, params=params)
        data = response.json()
        movie_titles.append({"movie_id": movie_id, "movie_title": data["title"]})

    return movie_titles


def config_api():
    """Call to TMDB configuration API.  Used to pull the image location data."""
    url = BASE_URL + "configuration"
    params = {"api_key": TMDB_KEY}

    response = requests.get(url, params=params)

    config = response.json()

    return config


def movie_info(movie_id):
    """Calls TMDB API to get the movie title, tagline, and genres"""
    url = BASE_URL + "movie/" + movie_id
    params = {
        "api_key": TMDB_KEY,
    }

    response = requests.get(url, params=params)

    data = response.json()

    return data


def movie_img(movie_id):
    """Calls TMDB API to get the url for the movie poster image hosted by TMDB"""
    config = config_api()
    url = BASE_URL + "movie/" + movie_id + "/images"

    params = {
        "api_key": TMDB_KEY,
    }
    response = requests.get(url, params=params)
    img = response.json()
    img_url = (
        config["images"]["base_url"]
        + config["images"]["poster_sizes"][2]
        + img["posters"][1]["file_path"]
    )

    return img_url


def media_wiki(movie_id):
    """Calls the wikipedia api to get the wikipedia url for the movie"""
    movie_name = movie_info(movie_id)
    api_endpoint = "https://en.wikipedia.org/w/api.php"
    search_page = movie_name["title"]
    params = {
        "action": "opensearch",
        "namespace": "0",
        "limit": "1",
        "search": search_page,
        "format": "json",
    }

    response = requests.get(api_endpoint, params=params)

    wiki_search = response.json()

    return wiki_search[3][0]
