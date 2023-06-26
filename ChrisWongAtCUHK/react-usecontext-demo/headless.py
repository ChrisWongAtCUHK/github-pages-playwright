from playwright.sync_api import Page, expect

def test_usecontext(page: Page) -> None:
    page.goto("https://chriswongatcuhk.github.io/React-useContext-Demo/")
    page.get_by_role("button", name="+").first.click()
    page.get_by_role("button", name="+").first.click()
    page.get_by_role("button", name="+").first.click()
    page.get_by_role("button", name="+").nth(1).click(click_count=2)
    page.get_by_role("button", name="-").first.click()
    page.get_by_role("button", name="-").nth(1).click()
    page.close()
