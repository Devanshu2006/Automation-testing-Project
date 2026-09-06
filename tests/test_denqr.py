from playwright.sync_api import expect


def test_denqr_home_page(page):

    page.goto(
        "https://denqr.onrender.com",
        wait_until="domcontentloaded",
        timeout=120000
    )

    expect(page).to_have_url("https://denqr.onrender.com/")

    expect(page.get_by_role("link", name="Login")).to_be_visible(timeout=120000)