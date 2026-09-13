import os

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


def get_config(environment):
    if environment not in ENVIRONMENTS:
        raise ValueError(
            f"Invalid environment: {environment}. "
            f"Choose from: {list(ENVIRONMENTS.keys())}"
        )

    return ENVIRONMENTS[environment]


API_TOKEN = os.getenv("API_TOKEN")