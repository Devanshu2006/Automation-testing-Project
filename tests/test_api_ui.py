from playwright.sync_api import expect


def test_api_then_ui(playwright, page):

    # API request
    request = playwright.request.new_context(
        base_url="https://jsonplaceholder.typicode.com"
    )

    response = request.get("/users/1")

    assert response.status == 200

    user = response.json()

    assert user["id"] == 1

    # UI
    page.goto("https://www.saucedemo.com/")

    expect(page).to_have_title("Swag Labs")

    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")

    page.get_by_role(
        "button",
        name="Login"
    ).click()

    expect(page.get_by_text("Products")).to_be_visible()

    request.dispose()