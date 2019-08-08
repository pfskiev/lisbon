import json

from django.core.exceptions import ValidationError
from django.test import TestCase, RequestFactory

from lisbon.forms import contains_html_tags
from lisbon.views import welcome


class SimpleTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_request(self):
        request = self.factory.get('/welcome')
        response = welcome(request)
        self.assertEqual(response.status_code, 405)

    def test_put_request(self):
        request = self.factory.put('/welcome')
        response = welcome(request)
        self.assertEqual(response.status_code, 405)

    def test_patch_request(self):
        request = self.factory.patch('/welcome')
        response = welcome(request)
        self.assertEqual(response.status_code, 405)

    def test_delete_request(self):
        request = self.factory.delete('/welcome')
        response = welcome(request)
        self.assertEqual(response.status_code, 405)

    def test_post_request_success(self):
        request = self.factory.post(
            path='/welcome',
            data=json.dumps({
                "name": "Alan    ",
                "email": "   test@test.com    ",
                "message": "Some message   ",
                "additionalInformation": ""}),
            content_type='application/json')
        response = welcome(request)
        self.assertEqual(response.status_code, 200)

    def test_post_request_failed(self):
        request = self.factory.post(
            path='/welcome',
            data=json.dumps({
                "name": "Alan    ",
                "email": "   test@test.com    ",
                "message": "Some message   ",
                "additionalInformation": " t"}),
            content_type='application/json')
        response = welcome(request)
        self.assertEqual(response.status_code, 422)

    def test_contains_html_tag_success(self):
        self.assertEqual(contains_html_tags('test   '), None)

    def test_contains_html_tag_failed(self):
        self.assertRaises(contains_html_tags('test <a>Link<a>   '), ValidationError)
