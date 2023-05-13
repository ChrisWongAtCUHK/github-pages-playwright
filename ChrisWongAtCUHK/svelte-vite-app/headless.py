from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chriswongatcuhk.github.io/svelte-vite-app/")
    page.screenshot(path="svelte-vite-app_0.png")
    page.get_by_role("button", name="count is 0").click()
    page.screenshot(path="svelte-vite-app_1.png")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
