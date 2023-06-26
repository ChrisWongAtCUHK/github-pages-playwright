from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://chriswongatcuhk.github.io/7-Event-Modifiers-in-Svelte-You-Must-Know/")
    page.get_by_role("checkbox").click()
    page.screenshot(path="7-Event-Modifiers-in-Svelte-You-Must-Know_preventDefault.png")
    page.close()
