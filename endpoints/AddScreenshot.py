from framework.API import API
from framework.utils.screenshooter import Screenshooter


class AddScreenshot(API):
    ENDPOINT = 'test/put/attachment'

    def add_screenshot(self, test_id):
        Screenshooter().set_session_screen_dir()
        content = Screenshooter().create_screenshot_string()
        self.post(self.ENDPOINT, data={'testId': test_id,
                                       'content': content,
                                       'contentType': 'image/png'})
