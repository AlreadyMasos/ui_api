from framework.pages.base_page import BasePage
from framework.elements.button import Button


class ProjectsPage(BasePage):

    nexage_button = Button('xpath', '//a[@href="allTests?projectId=1"]', 'nex_button')

    def __init__(self):
        super().__init__(self.nexage_button.get_search_condition(),
                         self.nexage_button.get_locator(),
                         'ProjectsPage')

    def click_nexage_button(self):
        self.nexage_button.click()