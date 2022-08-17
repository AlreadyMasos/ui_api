from framework.API import API


class CreateTest(API):

    ENDPOINT = 'test/put/'

    def create_test(self, sid, project_name, test_name, method_name, env):
        self.post(self.ENDPOINT, data={'SID': sid,
                                              'projectName': project_name,
                                              'testName': test_name,
                                              'methodName': method_name,
                                              'env': env})
        return self.get_text()
