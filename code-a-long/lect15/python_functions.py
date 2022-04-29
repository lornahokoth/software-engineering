"""
Activity: try to write unit tests for the below functions!
"""
import random
import requests

BASE_URL = "https://api.themoviedb.org/3/movie/

def get_movie_url(movie_ids):
    if movie_ids == None:
        return None
        
    movie_id = random.choice(movie_ids)
    return BASE_URL + movie_id

def get_movie_genres(url):
    response = requests.get(
        url,
        # We have to skip this line for this code to work without a .env file.
        # Since we'll be mocking out requests.get anyway, it doesn't matter!
        # params={
        #     "api_key": os.getenv("TMDB_API_KEY"),
        # },
    )
    json_response = response.json()
    genres = ", ".join(genre["name"] for genre in json_response["genres"])
    return genres