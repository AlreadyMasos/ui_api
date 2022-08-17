from framework.pages.base_page import BasePage
from framework.elements.button import Button
from framework.elements.text_box import TextBox
from framework.elements.text import Text
from framework.utils.string_util import set_random_string


class AddProjectPage(BasePage):

    input_pr_name = TextBox('xpath', '//input[@name="projectName"]', 'input_name')
    save_button = Button('xpath', '//button[@class="btn btn-primary"]', 'save_button')
    success_text = Text('xpath', '//div[@class="alert alert-success"]', 'suc_text')

    def __init__(self):
        super().__init__(self.input_pr_name.get_search_condition(),
                         self.input_pr_name.get_locator(),
                         'add project page')

    def insert_project_name(self):
        self.input_pr_name.wait_for_clickable()
        name = set_random_string()
        self.input_pr_name.send_text(name)
        return name

    def save_project(self):
        self.save_button.click()

    def check_success(self):
        self.success_text.wait_for_is_visible()
        return self.success_text.is_exist()
    