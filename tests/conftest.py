import pytest
from framework.browser.browser import Browser
from framework.utils.config_parser import ConfigParser


CONFIG = ConfigParser().get_config()


@pytest.fixture(scope='session')
def start_session():
    browser = Browser()
    browser.set_up_driver()
    browser.set_url(CONFIG['host_ui'])

