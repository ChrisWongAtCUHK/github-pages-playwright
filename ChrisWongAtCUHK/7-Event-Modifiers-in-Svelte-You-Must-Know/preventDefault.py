from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chriswongatcuhk.github.io/7-Event-Modifiers-in-Svelte-You-Must-Know/")
    page.get_by_role("checkbox").click()
    page.screenshot(path="7-Event-Modifiers-in-Svelte-You-Must-Know_preventDefault.png")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
