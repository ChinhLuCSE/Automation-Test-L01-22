#Author: Bui Ngoc Thanh Son - 1712961

import unittest
from TestUtils import TestEditProfile

class EditProfileSuite(unittest.TestCase):
    def test_0(self):
        """Normal"""
        username = "student"
        password = "moodle"
        firstname = "Optimus"
        lastname = "Prime"
        expect = "Optimus Prime"
        self.assertTrue(TestEditProfile.testEditSubmit(username, password, firstname, lastname, expect))

    def test_1(self):
        """Empty firstname"""
        username = "student"
        password = "moodle"
        firstname = ""
        lastname = "Prime"
        expect = "Barbara Gardner"
        self.assertTrue(TestEditProfile.testEditSubmit(username, password, firstname, lastname, expect))

    def test_2(self):
        """Empty lastname"""
        username = "student"
        password = "moodle"
        firstname = "Optimus"
        lastname = ""
        expect = "Barbara Gardner"
        self.assertTrue(TestEditProfile.testEditSubmit(username, password, firstname, lastname, expect))

    def test_3(self):
        """Empty both"""
        username = "student"
        password = "moodle"
        firstname = ""
        lastname = ""
        expect = "Barbara Gardner"
        self.assertTrue(TestEditProfile.testEditSubmit(username, password, firstname, lastname, expect))

    def test_4(self):
        """Normal"""
        username = "student"
        password = "moodle"
        firstname = "Optimus"
        lastname = "Prime"
        expect = "Barbara Gardner"
        self.assertTrue(TestEditProfile.testEditCancel(username, password, firstname, lastname, expect))

    def test_5(self):
        """Empty firstname"""
        username = "student"
        password = "moodle"
        firstname = ""
        lastname = "Prime"
        expect = "Barbara Gardner"
        self.assertTrue(TestEditProfile.testEditCancel(username, password, firstname, lastname, expect))

    def test_6(self):
        """Empty lastname"""
        username = "student"
        password = "moodle"
        firstname = "Optimus"
        lastname = ""
        expect = "Barbara Gardner"
        self.assertTrue(TestEditProfile.testEditCancel(username, password, firstname, lastname, expect))

    def test_7(self):
        """Empty both"""
        username = "student"
        password = "moodle"
        firstname = ""
        lastname = ""
        expect = "Barbara Gardner"
        self.assertTrue(TestEditProfile.testEditCancel(username, password, firstname, lastname, expect))