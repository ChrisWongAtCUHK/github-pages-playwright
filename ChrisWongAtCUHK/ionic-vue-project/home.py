from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://chriswongatcuhk.github.io/ionic-vue-project")
    page.screenshot(path="ionic-vue-project_home.png")
    page.close()
