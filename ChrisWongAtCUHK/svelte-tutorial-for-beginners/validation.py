from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chriswongatcuhk.github.io/svelte-tutorial-for-beginners/")
    page.get_by_text("Add New Poll").click()
    page.get_by_role("button", name="Add Poll").click()
    page.screenshot(path="svelte-tutorial-for-beginners_validation.png")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
