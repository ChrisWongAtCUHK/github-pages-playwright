from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://chriswongatcuhk.github.io/React-useContext-Demo/")
    page.get_by_role("button", name="+").first.click()
    page.get_by_role("button", name="+").first.click()
    page.get_by_role("button", name="+").first.click()
    page.screenshot(path="react-usecontext-demo_01.png")
    page.get_by_role("button", name="+").nth(1).click(click_count=2)
    page.screenshot(path="react-usecontext-demo_02.png")
    page.get_by_role("button", name="-").first.click()
    page.screenshot(path="react-usecontext-demo_03.png")
    page.get_by_role("button", name="-").nth(1).click()
    page.screenshot(path="react-usecontext-demo_04.png")
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
