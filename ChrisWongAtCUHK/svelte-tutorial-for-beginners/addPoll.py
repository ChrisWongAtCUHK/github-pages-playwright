from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chriswongatcuhk.github.io/svelte-tutorial-for-beginners/")
    page.get_by_text("Add New Poll").click()
    page.get_by_label("Poll Question:").click()
    page.get_by_label("Poll Question:").fill("Which one?")
    page.get_by_label("Answer A:").fill("apple")
    page.get_by_label("Answer B:").fill("boy")
    page.get_by_role("button", name="Add Poll").click()
    page.screenshot(path="svelte-tutorial-for-beginners_addPoll1.png")
    page.locator("div").filter(has_text="apple (0)").nth(4).click()
    page.locator("div").filter(has_text="apple (1)").nth(4).click()
    page.locator("div").filter(has_text="apple (2)").nth(4).click()
    page.locator("div").filter(has_text="apple (3)").nth(4).click()
    page.locator("div").filter(has_text="apple (4)").nth(4).click()
    page.locator("div").filter(has_text="apple (5)").nth(4).click()

    page.locator("div").filter(has_text="boy (0)").nth(4).click()
    page.locator("div").filter(has_text="boy (1)").nth(4).click()
    page.locator("div").filter(has_text="boy (2)").nth(4).click()
    page.screenshot(path="svelte-tutorial-for-beginners_addPoll2.png")
    page.pause()
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
