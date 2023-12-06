import unittest
from TestUtils import TestCreateEvent


class CreateEventSuite(unittest.TestCase):
    def test_1(self):
        """Leave Event Title blank"""
        title = ""
        description = ""
        expect = "- Required"
        self.assertTrue(TestCreateEvent.test(title, description, expect, 101))

    def test_2(self):
        """Fill Event Title"""
        title = "temp title"
        description = ""
        expect = "Successfully create an event"
        self.assertTrue(TestCreateEvent.testWithToken(title, description, expect, 102))

    def test_3(self):
        """Fill Event Title and Event Description"""
        title = ""
        description = "asdfasdf"
        expect = "- Required"
        self.assertTrue(TestCreateEvent.testWithToken(title, description, expect, 103))