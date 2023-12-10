import sys, os

sys.path.append("./test/")

import unittest


def main(argv):
    if len(argv) < 1:
        printUsage()
    elif argv[0] == "test":
        if len(argv) < 2:
            printUsage()
        elif argv[1] == "CreateEventSuite":
            from CreateEventSuite import CreateEventSuite
            getAndTest(CreateEventSuite)
        elif argv[1] == "ExportCalendarSuite":
            from ExportCalendarSuite import ExportCalendarSuite
            getAndTest(ExportCalendarSuite)
        elif argv[1] == "EditProfileSuite":
            from EditProfileSuite import EditProfileSuite
            getAndTest(EditProfileSuite)
        elif argv[1] == "ForumPostSuite":
            from ForumPostSuite import ForumPostSuite
            getAndTest(ForumPostSuite)
        elif argv[1] == "AssignmentSuite":
            from AssignmentSuite import AssignmentSuite
            getAndTest(AssignmentSuite)
        else:
            printUsage()
    else:
        printUsage()


def getAndTest(cls):
    suite = unittest.makeSuite(cls)
    test(suite)


def test(suite):
    from pprint import pprint
    from io import StringIO

    stream = StringIO()
    runner = unittest.TextTestRunner(stream=stream)
    result = runner.run(suite)
    print("Tests run ", result.testsRun)
    print("Errors ", result.errors)
    pprint(result.failures)
    stream.seek(0)
    print("Test output\n", stream.read())


def printUsage():
    print("python3 run.py test LoginSuite")
    print("python3 run.py test ChangePasswordSuite")
    print("python3 run.py test EditProfileSuite")
    print("python3 run.py test AssignmentsSuite")


if __name__ == "__main__":
    main(sys.argv[1:])
