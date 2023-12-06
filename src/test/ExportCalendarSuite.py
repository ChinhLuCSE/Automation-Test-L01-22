import unittest
from TestUtils import TestExportCalendar


class ExportCalendarSuite(unittest.TestCase):
    def test_1(self):
        """Empty Event to export and Time period"""
        event_to_export=""
        time_period=""
        expect = "Required"
        self.assertTrue(
            TestExportCalendar.test(
                event_to_export, time_period, expect, 201
            )
        )

    def test_2(self):
        """Not empty Event to export and Time period"""
        event_to_export="All events"
        time_period="This week"
        expect = "Successfully export calendar"

        self.assertTrue(
            TestExportCalendar.test(
                event_to_export, time_period, expect, 202
            )
        )

    def test_3(self):
        """Not empty Event to export and Time period"""
        event_to_export="Events related to categories"
        time_period="This month"
        expect = "Successfully export calendar"

        self.assertTrue(
            TestExportCalendar.test(
                event_to_export, time_period, expect, 203
            )
        )

    def test_4(self):
        """Not empty Event to export and Time period"""
        event_to_export="Events related to courses"
        time_period="Recent and next 60 days"
        expect = "Successfully export calendar"

        self.assertTrue(
            TestExportCalendar.test(
                event_to_export, time_period, expect, 204
            )
        )