import os

ENV = os.getenv("TEST_ENV", "qa")

ENVIRONMENTS = {
    "dev": {
        "api_base_url": "https://jsonplaceholder.typicode.com"
    },
    "qa": {
        "api_base_url": "https://jsonplaceholder.typicode.com"
    },
    "staging": {
        "api_base_url": "https://jsonplaceholder.typicode.com"
    }
}

API_BASE_URL = ENVIRONMENTS[ENV]["api_base_url"]
API_TOKEN = os.getenv("API_TOKEN")