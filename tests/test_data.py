LOGIN_TEST_DATA = [
    ("standard_user", "secret_sauce", True),
    ("wrong_user", "wrong_password", False),
    ("standard_user", "wrong_password", False),
    ("", "secret_sauce", False),
    ("standard_user", "", False),
]

USERS = [
    ("standard_user", "secret_sauce"),
    ("performance_glitch_user", "secret_sauce"),
]