import unittest

from run_app import app


class FlaskPracticeTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_1_welcome_view(self):
        response = self.client.get('/')
        assert (response.data) == b'Welcome to our Flask Practice!'

    def test_2_sum_two_numbers(self):
        response = self.client.get('/sum/100/200')
        assert (response.data) == b'The sum of 100 and 200 is: 300'

    def test_3_build_username(self):
        response = self.client.get('/username/Elon/Musk')
        assert (response.data) == b'emusk'

    def test_4_search_user(self):
        response = self.client.get('/user?search=mo')
        assert (response.data) == b'Found 2 users that match with search: "mo"'
