from framework.pages.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.elements.text import Text


class ProjectsPage(BasePage):

    nexage_button = Button('xpath', '//a[@href="allTests?projectId=1"]', 'nex_button')
    add_button = Button('xpath', '//a[@class="btn btn-xs btn-primary pull-right"]', 'add_button')
    footer = Text('xpath', '//span', 'footer')
    list_of_projects = Text('xpath', '//a[@class="list-group-item"]', 'list_of_projects')

    def __init__(self):
        super().__init__(self.nexage_button.get_search_condition(),
                         self.nexage_button.get_locator(),
                         'ProjectsPage')

    def click_nexage_button(self):
        self.nexage_button.click()

    def click_add_button(self):
        self.add_button.click()

    def check_variant(self):
        return '2' in self.footer.get_text()

    def count_projects(self):
        return self.list_of_projects.get_elements_count()

    def check_current_project_button(self):
        current_project_button = Button('xpath',
                                        f'//a[@href="allTests?projectId={self.count_projects() + 1}"]',
                                        'current_project_button')
        return current_project_button.is_exist()

    def click_current_project_button(self):
        current_project_button = Button('xpath',
                                        f'//a[@href="allTests?projectId={self.count_projects() + 1}"]',
                                        'current_project_button')
        return current_project_button.click()
