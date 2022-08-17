from framework.API import API
from framework.utils.log_parser import LoggerParser


class AddLogs(API):

    ENDPOINT = 'test/put/log'

    def add_logs(self, test_id):
        self.post(self.ENDPOINT, data={'testId': test_id,
                                       'content': LoggerParser().get_logs()})
        return self.get_status_code()
