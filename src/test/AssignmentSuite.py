import unittest
from TestUtils import TestAssignment



class AssignmentSuite(unittest.TestCase):
    def test_1(self):
        page="//div[@id='yui_3_18_1_1_1702222360241_35']/div[4]/a/div"
        assignment="(//a[contains(@href, 'https://school.moodledemo.net/mod/assign/view.php?id=775')])[4]"
        content="<p>123456</p>"
        expect = "Successfully submit assignment"
        self.assertTrue(
            TestExportCalendar.test(
                page, assignment, content, expect, 701
            )
        )

    def test_2(self):
        page="//div[@id='yui_3_18_1_1_1702222360241_35']/div[4]/a/div"
        assignment="(//a[contains(@href, 'https://school.moodledemo.net/mod/assign/view.php?id=775')])[4]"
        content=""
        expect = "Successfully remove assignment"
        self.assertTrue(
            TestExportCalendar.test(
                page, assignment, content, expect, 702
            )
        )

    def test_3(self):
        page="//div[@id='page-container-2']/div/div/div[10]/a/div"
        assignment="(//a[contains(@href, 'https://school.moodledemo.net/mod/assign/view.php?id=748')])[3]"
        content="<p>123456</p>"
        expect = "Successfully submit assignment"
        self.assertTrue(
            TestExportCalendar.test(
                page, assignment, content, expect, 703
            )
        )