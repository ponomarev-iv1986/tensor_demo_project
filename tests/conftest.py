import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import config
from tensor_demo_project.utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    if config.settings.ENVIRONMENT == 'local':
        browser.config.base_url = 'https://tensor.ru'
        browser.config.window_width = 1400
        browser.config.window_height = 800
        driver_options = webdriver.ChromeOptions()
        browser.config.driver = driver_options

    else:
        browser.config.base_url = 'https://tensor.ru'
        options = Options()
        selenoid_capabilities = {
            'browserName': 'chrome',
            'browserVersion': '100',
            'selenoid:options': {
                'enableVNC': False,
                'enableVideo': False
            }
        }
        options.capabilities.update(selenoid_capabilities)

        login = config.settings.LOGIN
        password = config.settings.PASSWORD

        driver = webdriver.Remote(
            command_executor=f'https://{login}:{password}@selenoid.autotests.cloud/wd/hub',
            options=options)

        browser.config.driver = driver

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    if config.settings.ENVIRONMENT == 'remote':
        attach.add_video(browser)

    browser.quit()
