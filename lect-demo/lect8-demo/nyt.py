import requests
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())  # This is to load your API keys from .env

BASE_URL = "https://api.nytimes.com/svc/search/v2/articlesearch.json"


def article_search(query):
    params = {
        "q": query,  # Query keywords
        "api-key": os.getenv("NYT_KEY"),
    }

    response = requests.get(
        BASE_URL,
        params=params,
    )

    headlines = []
    snippets = []

    # Print headlines for first 10 articles returned by search endpoint
    articles = response.json()["response"]["docs"]
    for article in articles:
        headlines.append(article["headline"]["main"])
        snippets.append(article["snippet"])

    return headlines, snippets
