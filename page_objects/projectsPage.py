from framework.pages.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.elements.text import Text
from framework.utils.string_util import set_random_string


class ProjectsPage(BasePage):

    nexage_button = Button('xpath', '//a[@href="allTests?projectId=1"]', 'nex_button')
    add_button = Button('xpath', '//a[@class="btn btn-xs btn-primary pull-right"]', 'add_button')
    footer = Text('xpath', '//footer[@class="footer"]', 'footer')

    def __init__(self):
        super().__init__(self.nexage_button.get_search_condition(),
                         self.nexage_button.get_locator(),
                         'ProjectsPage')

    def click_nexage_button(self):
        self.nexage_button.click()

    def click_add_button(self):
        self.add_button.click()
