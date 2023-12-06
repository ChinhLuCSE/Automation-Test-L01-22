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

    def test_1(self):
        """Only White Space"""
        username = "student"
        password = "moodle"
        title = """    """
        content = """    """
        expect = ""
        self.assertTrue(TestForumPost.testCreatePost(username, password, title, content, expect))

    def test_2(self):
        """Empty both"""
        username = "student"
        password = "moodle"
        title = ""
        content = ""
        expect = ""
        self.assertTrue(TestForumPost.testCreatePost(username, password, title, content, expect))