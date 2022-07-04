from unittest import TestCase
from unittest.mock import patch
from page import PageRequester


class TestPageRequester(TestCase):
    def setUp(self):
        self.page = PageRequester('https://google.com')

    def test_make_request(self):
        with patch('requests.get') as mocked_get:
            self.page.get()
            mocked_get.assert_called()
