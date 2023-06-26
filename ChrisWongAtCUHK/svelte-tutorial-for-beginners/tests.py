from playwright.sync_api import Page, expect

def test_addPoll(page: Page) -> None:
    page.goto("https://chriswongatcuhk.github.io/svelte-tutorial-for-beginners/")
    page.get_by_text("Add New Poll").click()
    page.get_by_label("Poll Question:").click()
    page.get_by_label("Poll Question:").fill("Which one?")
    page.get_by_label("Answer A:").fill("apple")
    page.get_by_label("Answer B:").fill("boy")
    page.get_by_role("button", name="Add Poll").click()
    page.locator("div.answer").first.click()
    page.locator("div.answer").first.click()
    page.locator("div.answer").first.click()
    page.locator("div.answer").nth(1).click()
    page.locator("div.answer").nth(1).click()
    page.locator("div.answer").nth(1).click()
    page.locator("div.answer").nth(1).click()
    page.close()

def test_deletePoll(page: Page) -> None:
    page.goto("https://chriswongatcuhk.github.io/svelte-tutorial-for-beginners/")
    page.get_by_text("Add New Poll").click()
    page.get_by_label("Poll Question:").click()
    page.get_by_label("Poll Question:").fill("Which one?")
    page.get_by_label("Answer A:").fill("apple")
    page.get_by_label("Answer B:").fill("boy")
    page.get_by_role("button", name="Add Poll").click()
    page.get_by_role("button", name="Delete").first.click()
    page.get_by_role("button", name="Delete").first.click()