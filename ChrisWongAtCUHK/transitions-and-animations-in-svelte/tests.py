from playwright.sync_api import Page, expect


def test_elasticout(page: Page) -> None:
    page.goto("https://chriswongatcuhk.github.io/transitions-and-animations-in-svelte/")
    page.get_by_label("Showing").check()
    page.get_by_label("Showing").uncheck()

def test_fade(page: Page) -> None:
    page.goto("https://chriswongatcuhk.github.io/transitions-and-animations-in-svelte/")
    page.get_by_text("Fade").click()
    page.get_by_label("Showing").check()
    page.get_by_label("Showing").uncheck()
