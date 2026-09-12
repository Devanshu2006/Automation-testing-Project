import os

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://jsonplaceholder.typicode.com"
)

API_TOKEN = os.getenv("API_TOKEN")