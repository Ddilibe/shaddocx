from unittest import TestCase
from utils.urlutils import url_valid


class URLTest(TestCase):
    def test_url_not_working_without_http_protocol(self):
        """Test that the url will not work with out the httpp and https protocol"""
        self.assertFalse(url_valid("github.com"))
        self.assertFalse(url_valid("wikipedia.com"))

    def test_url_works_with_http_protocole(self):
        """Test that url will work with the http and https protocol"""
        self.assertTrue(url_valid("https://www.github.com"))
        self.assertTrue(url_valid("https://chat.openai.com/"))
