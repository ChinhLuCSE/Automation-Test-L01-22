#Author: Bui Ngoc Thanh Son - 1712961

import unittest
from TestUtils import TestForumPost

class ForumPostSuite(unittest.TestCase):
    def test_0(self):
        """Normal"""
        username = "student"
        password = "moodle"
        title = "abc"
        content = "xyz"
        expect = "Your post was successfully added."
        self.assertTrue(TestForumPost.testCreatePost(username, password, title, content, expect))