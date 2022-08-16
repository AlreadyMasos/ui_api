from framework.browser.browser import Browser
from framework.utils.config_parser import ConfigParser
from endpoints.firstProjectJSON import firstProjJson
from endpoints.GetToken import Token
from framework.API import API
from page_objects.projectsPage import ProjectsPage
from page_objects.nexagePage import NexagePage

CONFIG = ConfigParser().get_config()


def test():
    token = Token().get_token()
    assert token != '0'
    browser = Browser()
    browser.set_up_driver()
    browser.set_url(CONFIG['host_ui'])
    m = API()
    #m.post(link=2, endpoint='http://login:password@localhost:9090/web/projects', cookies=
    #        {'token': token})
    #browser.refresh_page()
    projects_page = ProjectsPage()
    projects_page.click_nexage_button()
    first = firstProjJson()
    #get = first.get_json_tests()
    #print(get)
    nex_Page = NexagePage()
    print(nex_Page.get_test_names())
    print(nex_Page.get_data_time())
    print(nex_Page.check_if_dates_sorted())

