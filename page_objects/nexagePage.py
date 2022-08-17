from framework.pages.base_page import BasePage
from framework.elements.table import Table
from framework.utils.datetime_util import DatetimeUtil
from framework.utils.config_parser import ConfigParser


class NexagePage(BasePage):

    CONFIG = ConfigParser().get_config()

    test_table = Table('xpath', '//table[@class="table"]', 'test_table')

    def __init__(self):
        super().__init__(self.test_table.get_search_condition(),
                         self.test_table.get_locator(),
                         'NexagePage')

    def get_test_names(self):
        self.test_table.wait_for_is_displayed(self.CONFIG['implicitly_wait_sec'])
        return self.test_table.get_cloumn_data('test name')

    def get_data_time(self):
        self.test_table.wait_for_is_displayed(self.CONFIG['implicitly_wait_sec'])
        return self.test_table.get_cloumn_data('test time')

    def check_if_dates_sorted(self):
        self.test_table.wait_for_is_present()
        return DatetimeUtil().check_if_dates_sorted(self.get_data_time())

    def check_if_data_correct(self, json_response):
        self.test_table.wait_for_is_present()
        return self.get_test_names() in json_response
