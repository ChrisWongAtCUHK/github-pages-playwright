from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chriswongatcuhk.github.io/svelte-tutorial-for-beginners/")
    page.get_by_text("Add New Poll").click()
    page.get_by_label("Poll Question:").click()
    page.get_by_label("Poll Question:").fill("Which one?")
    page.get_by_label("Answer A:").fill("apple")
    page.get_by_label("Answer B:").fill("boy")
    page.get_by_role("button", name="Add Poll").click()
    page.screenshot(path="svelte-tutorial-for-beginners_deletePoll1.png")
    page.get_by_role("button", name="Delete").first.click()
    page.screenshot(path="svelte-tutorial-for-beginners_deletePoll2.png")
    page.get_by_role("button", name="Delete").first.click()
    page.screenshot(path="svelte-tutorial-for-beginners_deletePoll3.png")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)