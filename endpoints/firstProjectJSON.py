from framework.API import API


class firstProjJson(API):

    ENDPOINT = 'test/get/json'

    def get_json_tests(self):
        self.post(endpoint=self.ENDPOINT+'?projectId=1')
        return self.get_json()

    def find_test_names(self):
        names = [i['name'] for i in self.get_json_tests()]
        return names
