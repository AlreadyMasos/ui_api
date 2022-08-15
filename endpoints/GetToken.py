from framework import API


class Token(API):

    ENDPOINT = 'token/get'

    def get_token(self):
        self.get(self.ENDPOINT)
        return self.get_json()
