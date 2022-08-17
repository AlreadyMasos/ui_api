from framework.API import API
from framework.utils.dataset_parser import DataSetParser
from framework.utils.string_util import set_random_string


class CreateTest(API):

    ENDPOINT = 'test/put/'
    DATA = DataSetParser().get_dataset()

    def create_test(self):
        self.post(self.ENDPOINT, data={'SID': set_random_string(),
                                       'projectName': self.DATA['project_name'],
                                       'testName': self.DATA['test_name'],
                                       'methodName': self.DATA['method_name'],
                                       'env': self.DATA['env']})
        return self.get_text()
