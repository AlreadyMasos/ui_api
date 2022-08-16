from framework.API import API


class Token(API):

    ENDPOINT = 'token/get'

    def get_token(self):
        self.post(self.ENDPOINT+'?variant=2')
        return self.get_cookie()
