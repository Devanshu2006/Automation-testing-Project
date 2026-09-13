import os
import pytest

from config import API_TOKEN, get_config
from api.api_client import ApiClient


@pytest.fixture(scope="function")
def logged_in_page(browser):
    context = browser.new_context(
        storage_state="auth/auth.json"
    )

    page = context.new_page()

    yield page

    context.close()


@pytest.fixture
def api_request(playwright, request):
    environment = request.config.getoption("--env")

    config = get_config(environment)

    api_request = playwright.request.new_context(
        base_url=config["api_base_url"]
    )

    yield api_request

    api_request.dispose()


@pytest.fixture
def api_client(api_request):
    return ApiClient(
        api_request,
        token=API_TOKEN
    )


def pytest_addoption(parser):
    parser.addoption(
        "--env",
        action="store",
        default="qa",
        help="Test environment: dev, qa, or staging"
    )


def pytest_configure(config):
    env = config.getoption("--env")
    os.environ["TEST_ENV"] = env