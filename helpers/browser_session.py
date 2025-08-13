from browser_use import BrowserSession
from browser_use.browser import BrowserProfile

browser_profile = BrowserProfile(
    headless=False,
    ad_blocker=True,
    user_data_dir='~/.config/browseruse/profiles/default',
    window_size={"width": 1920, "height": 1080},  # Browser window size
    browser_viewport_width=1280,
    browser_viewport_height=1080,
    wait_for_network_idle_page_load_time=1.0,  # Faster loading
    maximum_wait_page_load_time=5.0,
)

async def get_browser_session():
    browser_session = BrowserSession(browser_profile=browser_profile)
    await browser_session.start()
    return browser_session
