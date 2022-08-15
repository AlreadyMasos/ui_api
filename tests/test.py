from framework.browser.browser import Browser
from framework.utils.config_parser import ConfigParser
from tests.conftest import start_session
from endpoints.GetToken import Token
from framework.API import API
from page_objects.projectsPage import ProjectsPage
CONFIG = ConfigParser().get_config()


def test():
    token = Token().get_token()
    assert token != '0'
    browser = Browser()
    browser.set_up_driver()
    browser.set_url(CONFIG['host_ui'])
    m = API()
    m.post(link=2, endpoint='http://login:password@localhost:9090/web/projects', cookies=
            {'token': token})
    browser.refresh_page()
    projects_page = ProjectsPage()
    projects_page.click_nexage_button()

