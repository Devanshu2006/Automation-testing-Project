from pages.login_page import LoginPage


def test_save_auth_state(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(
        "standard_user",
        "secret_sauce"
    )

    page.context.storage_state(path="auth/auth.json")