import requests
import json
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

NYT_KEY = "Ao2QFooFkc1t4eI05k7O3EwBcPG3WnRl"
BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"


query_params = {
    "api-key": os.getenv("NYT_KEY"),
    "q": "florida man",
}

response = requests.get(
    BASE_URL,
    params=query_params
)
print(response)
