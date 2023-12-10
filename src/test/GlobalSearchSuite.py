import unittest
from TestUtils import TestGlobalSearch

class GlobalSearchSuite(unittest.TestCase):
    def test_0(self):
        """Normal"""
        query = "critical thinking"
        title = "Aristotle"
        expect = "Success"
        self.assertTrue(TestGlobalSearch.testGlobalSearch(query,title,expect))
    def test_1(self):
        """No Result"""
        query = "critical thinking"
        title = "Aristotlet"
        expect = "No Result"
        self.assertTrue(TestGlobalSearch.testGlobalSearch(query,title,expect))
    def test_2(self):
        """Required"""
        query = ""
        title = "Aristotlet"
        expect = "Require"
        self.assertTrue(TestGlobalSearch.testGlobalSearch(query,title,expect))
    