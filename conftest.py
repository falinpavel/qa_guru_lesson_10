import pytest

from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope="session", autouse=True)
def browser_options():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    # driver_options.add_argument('--window-size=1920,1080')
    driver_options.add_argument("--headless")  # для CI
    driver_options.add_argument("--no-sandbox")
    driver_options.add_argument("--disable-dev-shm-usage")
    driver_options.add_argument("--disable-gpu")
    return driver_options


@pytest.fixture(scope="class", autouse=True)
def browser_open_and_quit(browser_options):
    browser.config.driver_options = browser_options
    yield
    browser.quit()
