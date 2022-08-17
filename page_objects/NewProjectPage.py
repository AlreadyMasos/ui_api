from framework.pages.base_page import BasePage
from framework.elements.button import Button
from framework.elements.table import Table


class NewProjectPage(BasePage):

    add_button = Button('xpath', '//button[@data-target="#addTest"]', 'button')
    test_table = Table('xpath', '//table[@class]/tbody/tr', 'test table')

    def __init__(self):
        super().__init__(self.add_button.get_search_condition(),
                         self.add_button.get_locator(),
                         'NewProjectPage')

    def check_test_add(self):
        return self.test_table.row_count() > 2
