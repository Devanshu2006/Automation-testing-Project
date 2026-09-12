class ApiAssertions:

    @staticmethod
    def assert_status(response, expected_status):
        assert response.status == expected_status, (
            f"Expected status {expected_status}, "
            f"but got {response.status}"
        )

    @staticmethod
    def assert_success(response):
        assert 200 <= response.status < 300, (
            f"API request failed with status {response.status}"
        )

    @staticmethod
    def assert_json(response):
        content_type = response.headers.get("content-type", "")
        assert "application/json" in content_type, (
            f"Expected JSON response, got {content_type}"
        )