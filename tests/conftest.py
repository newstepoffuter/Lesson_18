import pytest
from selene import browser
from test_webshop.utils import attachment_type


@pytest.fixture(scope="function", autouse=True)
def browser_setting():
    browser.config.base_url = 'https://demowebshop.tricentis.com'
    browser.config.window_height = 1800
    browser.config.window_width = 1200

    yield browser

    attachment_type.create_html(browser)
    attachment_type.create_logs(browser)
    attachment_type.create_screenshot(browser)
    browser.quit()
