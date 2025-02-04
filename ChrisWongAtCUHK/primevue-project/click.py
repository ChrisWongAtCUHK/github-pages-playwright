from playwright.sync_api import Page


def test_example(page: Page) -> None:
    page.goto("https://chriswongatcuhk.github.io/primevue-project/")
    page.get_by_role("button", name="PrimeVue Button").click()
    page.screenshot(path="primevue-project_click.png")
    page.close()
