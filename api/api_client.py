import time

from utils.logger import get_logger


class ApiClient:

    RETRY_STATUS_CODES = {500, 502, 503, 504}

    def __init__(self, request, token=None):
        self.request = request
        self.logger = get_logger("ApiClient")

        self.headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }

        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    def get(self, endpoint, retries=3, **kwargs):
        response = None

        for attempt in range(1, retries + 1):

            self.logger.info(
                f"GET {endpoint} - Attempt {attempt}"
            )

            response = self.request.get(
                endpoint,
                headers=self.headers,
                **kwargs
            )

            self.logger.info(
                f"Response Status: {response.status}"
            )

            if response.status < 500:
                return response

            if response.status in self.RETRY_STATUS_CODES:

                if attempt < retries:
                    wait_time = 2 ** (attempt - 1)

                    self.logger.warning(
                        f"Retrying in {wait_time} seconds..."
                    )

                    time.sleep(wait_time)

            else:
                break

        return response

    def post(self, endpoint, **kwargs):
        self.logger.info(f"POST {endpoint}")

        response = self.request.post(
            endpoint,
            headers=self.headers,
            **kwargs
        )

        self.logger.info(
            f"Response Status: {response.status}"
        )

        return response

    def put(self, endpoint, **kwargs):
        self.logger.info(f"PUT {endpoint}")

        response = self.request.put(
            endpoint,
            headers=self.headers,
            **kwargs
        )

        self.logger.info(
            f"Response Status: {response.status}"
        )

        return response

    def patch(self, endpoint, **kwargs):
        self.logger.info(f"PATCH {endpoint}")

        response = self.request.patch(
            endpoint,
            headers=self.headers,
            **kwargs
        )

        self.logger.info(
            f"Response Status: {response.status}"
        )

        return response

    def delete(self, endpoint, **kwargs):
        self.logger.info(f"DELETE {endpoint}")

        response = self.request.delete(
            endpoint,
            headers=self.headers,
            **kwargs
        )

        self.logger.info(
            f"Response Status: {response.status}"
        )

        return response