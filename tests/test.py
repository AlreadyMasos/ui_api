from framework.browser.browser import Browser
from framework.utils.config_parser import ConfigParser
from endpoints.firstProjectJSON import firstProjJson
from endpoints.GetToken import Token
from endpoints.CreateTest import CreateTest
from endpoints.AddLogs import AddLogs
from endpoints.AddScreenshot import AddScreenshot
from page_objects.projectsPage import ProjectsPage
from page_objects.nexagePage import NexagePage
from page_objects.addProjectPage import AddProjectPage

CONFIG = ConfigParser().get_config()


def test():
    token = Token().get_token()
    assert token != '0', 'token not created'
    browser = Browser()
    browser.set_up_driver()
    browser.set_url(CONFIG['host_ui'])
    browser.add_cookie('token', token)
    browser.refresh_page()
    projects_page = ProjectsPage()
    assert projects_page.is_opened(), 'projects page not opened'
    assert projects_page.check_variant(), 'variant number not correct'
    projects_page.click_nexage_button()
    json_nexage_project = firstProjJson()
    nex_Page = NexagePage()
    assert nex_Page.check_if_dates_sorted(), 'dates sorted not correctly'
    assert nex_Page.check_if_data_correct(json_nexage_project.find_test_names())
    browser.back_page()
    projects_page.click_add_button()
    browser.switch_new_window()
    add_project_page = AddProjectPage()
    print(add_project_page.insert_project_name())
    add_project_page.save_project()
    assert add_project_page.check_success(), 'project not saved'
    browser.switch_to_window()
    browser.refresh_page()
    assert projects_page.check_current_project_button(), 'project not created'
    projects_page.click_current_project_button()
    test_id = CreateTest().create_test()
    AddLogs().add_logs(test_id)
    AddScreenshot().add_screenshot(test_id)
