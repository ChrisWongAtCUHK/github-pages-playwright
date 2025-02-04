from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chriswongatcuhk.github.io/primevue-project/")
    page.get_by_role("button", name="PrimeVue Button").click()
    page.screenshot(path="primevue-project_click.png")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
