from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig

async def get_browser_and_context():
    browser = Browser(config=BrowserConfig(headless=False))
    browser_context = BrowserContext(browser=browser, config=BrowserContextConfig())
    return browser, browser_context
