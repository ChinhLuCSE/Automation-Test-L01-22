import time
import sys, os
from unittest import result
from dotenv import find_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TEST_DIR = "./test/testcases/"
SOL_DIR = "./test/solutions/"

url = "https://school.moodledemo.net/"
LOGIN_BUTTON_XPATH = "//a[contains(@href, 'https://school.moodledemo.net/login/index.php')]"
STUDENT_TEACHER_XPATH = (
    """//*[@id="region-main"]/div/div/div/div/div[3]/p[1]/a"""
)
LOUGOUT_BUTTON_XPATH = (
    "//a[starts-with(@href, 'https://e-learning.hcmut.edu.vn/login/logout.php')]"
)
CHANGE_PASSWORD_LINK_XPATH = "//a[@href='https://account.hcmut.edu.vn/']"
CHANGE_PASSWORD_SUBMIT_XPATH = "//button[@type='submit']"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.maximize_window()


def goToLoginPage():
    driver.get(url)
    driver.find_element(By.XPATH, LOGIN_BUTTON_XPATH).click()


class TestUtil:
    @staticmethod
    def makeSource(inputStr, num):
        filename = TEST_DIR + str(num) + ".txt"
        file = open(filename, "w")
        file.write(inputStr)
        file.close()
    @staticmethod
    def login(username, password):
        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "loginbtn").click()



class TestCreateEvent:
    @staticmethod
    def test(title, description, expect, num):
        goToLoginPage()

        TestUtil.login("teacher", "moodle")

        input_str = """title: %s
description: %s
""" % (
            title,
            description,
        )
        TestUtil.makeSource(input_str, num)
        
        driver.find_element(By.ID, "user-menu-toggle").click()
        driver.find_element(By.LINK_TEXT, "Calendar").click()
        driver.find_element(By.XPATH, "//button[contains(.,'New event')]").click()
        TestCreateEvent.fillform(title, description)
        TestCreateEvent.check(SOL_DIR, num)
        
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect
    
    def testWithToken(title, description, expect, num):

        input_str = """title: %s
description: %s
""" % (
            title,
            description,
        )
        TestUtil.makeSource(input_str, num)
        
        driver.find_element(By.ID, "user-menu-toggle").click()
        driver.find_element(By.LINK_TEXT, "Calendar").click()
        driver.find_element(By.XPATH, "//button[contains(.,'New event')]").click()
        TestCreateEvent.fillform(title, description)
        TestCreateEvent.check(SOL_DIR, num)
        
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def check(soldir, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")

        result_eles = driver.find_element(By.ID, "id_error_name")
        if len(result_eles.text) == 0:
            dest.write("Successfully create an event")
            return
        dest.write(result_eles.text)
        driver.get(url)
        driver.refresh()

    @staticmethod
    def fillform(title, description):
        time.sleep(3)
        title_ele = driver.find_element(By.ID, "id_name")
        if title_ele.is_displayed():
            title_ele.send_keys(title)
        if len(description) != 0:
            driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
            driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
            time.sleep(5)
            driver.find_element(By.ID, "id_location").send_keys(description)
        driver.find_element(By.XPATH, "//button[contains(.,'Save')]").click()

class TestExportCalendar:
    @staticmethod
    def test(event_to_export, time_period, expect, num):
        goToLoginPage()

        TestUtil.login("teacher", "moodle")

        input_str = """event_to_export: %s
time_period: %s
""" % (
            event_to_export,
            time_period,
        )
        TestUtil.makeSource(input_str, num)
        
        driver.find_element(By.ID, "user-menu-toggle").click()
        driver.find_element(By.LINK_TEXT, "Calendar").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Import or export calendars')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Export calendar')]").click()
        
        if len(event_to_export) != 0:
            driver.find_element(By.XPATH, "//label[contains(.,{event_to_export})]").click()
        if len(time_period) != 0:
            driver.find_element(By.XPATH, "//label[contains(.,{time_period})]").click()
        driver.find_element(By.ID, "id_export").click()

        TestExportCalendar.check(SOL_DIR, num)
        
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect

    @staticmethod
    def testWithToken(event_to_export, time_period, expect, num):

        input_str = """event_to_export: %s
time_period: %s
""" % (
            event_to_export,
            time_period,
        )
        TestUtil.makeSource(input_str, num)
        
        driver.find_element(By.ID, "user-menu-toggle").click()
        driver.find_element(By.LINK_TEXT, "Calendar").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Import or export calendars')]").click()
        driver.find_element(By.XPATH, "//button[contains(.,'Export calendar')]").click()
        
        if len(event_to_export) != 0:
            temp_xpath="""//label[contains(.,'%s')]""" % (
                event_to_export
            )
            driver.find_element(By.XPATH, temp_xpath).click()
        if len(time_period) != 0:
            temp_xpath="""//label[contains(.,'%s')]""" % (
                time_period
            )
            driver.find_element(By.XPATH, temp_xpath).click()
        driver.find_element(By.ID, "id_export").click()

        TestExportCalendar.check(SOL_DIR, num)
        
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect
    
    @staticmethod
    def check(soldir, num):
        dest = open(os.path.join(soldir, str(num) + ".txt"), "w")

        result_event_ele = driver.find_element(By.ID, "fgroup_id_error_events")
        result_period_ele = driver.find_element(By.ID, "fgroup_id_error_period")
        if len(result_event_ele.text) == 0 and len(result_period_ele.text) == 0 :
            dest.write("Successfully export calendar")
            return
        dest.write("Required")
        driver.get(url)
        driver.refresh()

#Author: Bui Ngoc Thanh Son - 1712961
class TestEditProfile:
    @staticmethod
    def testEditSubmit(username, password, firstname, lastname, expect):
        TestEditProfile.submitEditProfile(username, password, firstname, lastname)
        check = TestEditProfile.check(expect)
        TestEditProfile.resetProfile()

        return check
    
    @staticmethod
    def testEditCancel(username, password, firstname, lastname, expect):
        TestEditProfile.cancelEditProfile(username, password, firstname, lastname)
        check = TestEditProfile.check(expect)
        TestEditProfile.resetProfile()

        return check
    
    @staticmethod
    def check(expect):
        driver.get("https://school.moodledemo.net/user/profile.php")
        result = driver.find_element(By.CSS_SELECTOR, "#page h1").text
        return result == expect
    
    @staticmethod
    def submitEditProfile(username, password, firstname, lastname):
        try:
            driver.get("https://school.moodledemo.net/login/index.php")
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "loginbtn").click()
        except Exception:
            pass

        driver.get("https://school.moodledemo.net/user/profile.php")
        driver.find_element(By.XPATH, "//a[@href='https://school.moodledemo.net/user/edit.php?id=56&returnto=profile']").click()
        driver.find_element(By.ID, "id_firstname").clear()
        driver.find_element(By.ID, "id_firstname").send_keys(firstname)
        driver.find_element(By.ID, "id_lastname").clear()
        driver.find_element(By.ID, "id_lastname").send_keys(lastname)
        driver.find_element(By.ID, "id_submitbutton").click()

    @staticmethod
    def cancelEditProfile(username, password, firstname, lastname):
        try:
            driver.get("https://school.moodledemo.net/login/index.php")
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "loginbtn").click()
        except Exception:
            pass

        driver.get("https://school.moodledemo.net/user/profile.php")
        driver.find_element(By.XPATH, "//a[@href='https://school.moodledemo.net/user/edit.php?id=56&returnto=profile']").click()
        driver.find_element(By.ID, "id_firstname").clear()
        driver.find_element(By.ID, "id_firstname").send_keys(firstname)
        driver.find_element(By.ID, "id_lastname").clear()
        driver.find_element(By.ID, "id_lastname").send_keys(lastname)
        driver.find_element(By.ID, "id_cancel").click()

    @staticmethod
    def resetProfile():
        driver.get("https://school.moodledemo.net/user/profile.php")
        driver.find_element(By.XPATH, "//a[@href='https://school.moodledemo.net/user/edit.php?id=56&returnto=profile']").click()
        driver.find_element(By.ID, "id_firstname").clear()
        driver.find_element(By.ID, "id_firstname").send_keys("Barbara")
        driver.find_element(By.ID, "id_lastname").clear()
        driver.find_element(By.ID, "id_lastname").send_keys("Gardner")
        driver.find_element(By.ID, "id_submitbutton").click()

#Author: Bui Ngoc Thanh Son
class TestForumPost:
    @staticmethod
    def testCreatePost(username, password, title, content, expect):
        TestForumPost.createPost(username, password, title, content)
        return TestForumPost.check(expect)

    @staticmethod
    def check(expect):
        arr = driver.find_elements(By.CSS_SELECTOR, "#user-notifications p")
        if len(arr) > 0:
            result = arr[0].text
        else:
            result = ""
        return result == expect
    
    @staticmethod
    def createPost(username, password, title, content):
        try:
            driver.get("https://school.moodledemo.net/login/index.php")
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "username").send_keys(username)
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys(password)
            driver.find_element(By.ID, "loginbtn").click()
        except Exception:
            pass

        driver.get("https://school.moodledemo.net/mod/forum/view.php?id=944")
        driver.find_element(By.XPATH, "//a[@href='#collapseAddForm']").click()
        driver.find_element(By.ID, "id_subject").clear()
        driver.find_element(By.ID, "id_subject").send_keys(title)
        WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "id_message_ifr")))
        driver.find_element(By.CSS_SELECTOR, "#tinymce").clear()
        driver.find_element(By.CSS_SELECTOR, "#tinymce").send_keys(content)
        driver.switch_to.default_content()
        driver.find_element(By.ID, "id_submitbutton").click()
#Author: Nguyễn Anh Khoa - 2011424
class TestGlobalSearch:
     
     
      @staticmethod
      def testGlobalSearch(query,title,expect):
        # goToLoginPage()
        # TestUtil.login("teacher", "moodle")
        try:
            driver.get("https://school.moodledemo.net/login/index.php")
            driver.find_element(By.ID, "username").clear()
            driver.find_element(By.ID, "username").send_keys("student")
            driver.find_element(By.ID, "password").clear()
            driver.find_element(By.ID, "password").send_keys("moodle")
            driver.find_element(By.ID, "loginbtn").click()
        except Exception:
            pass

        driver.get("https://school.moodledemo.net/search/index.php/search/index.php")
        driver.set_window_size(1440, 805)
        driver.find_element(By.ID, "id_q").click()
        driver.find_element(By.ID, "id_q").send_keys(query)
        driver.find_element(By.ID, "collapseElement-1").click()
        driver.find_element(By.XPATH, "//input[@id='id_title']").click()
        driver.find_element(By.ID, "id_title").send_keys(title)
        driver.find_element(By.XPATH, "//span[contains(.,'▼')]").click()
        driver.find_element(By.XPATH, "(//li[@id=''])[3]").click()
        
        driver.find_element(By.ID, "page").click()
        time.sleep(5)
        driver.find_element(By.ID, "id_timestart_label").click()
        driver.find_element(By.ID, "id_timestart_enabled").click()
        driver.find_element(By.ID, "id_timestart_month").click()
        dropdown = driver.find_element(By.ID, "id_timestart_month")
        dropdown.find_element(By.XPATH, "//option[. = 'January']").click()
        driver.find_element(By.ID, "id_timestart_year").click()
        dropdown = driver.find_element(By.ID, "id_timestart_year")
        dropdown.find_element(By.XPATH, "//option[. = '2009']").click()
        driver.find_element(By.ID, "id_timeend_enabled").click()
        driver.find_element(By.ID, "id_timeend_month").click()
        
        
        driver.execute_script("window.scrollTo(0,87)")
        driver.find_element(By.ID, "id_submitbutton").click()
        driver.execute_script("window.scrollTo(0,61)")

        time.sleep(3)
        return TestGlobalSearch.check(expect)

        
      @staticmethod
      def check(expect):
        
        if (expect=="Success"):
            if (driver.find_element(By.XPATH,"//a[contains(.,'Aristotle')]")) :
                return True
        elif (expect=="No Result"):
            if (driver.find_element(By.XPATH,"//section[@id='region-main']/div/div")):
                return True
        elif (expect=="Require"):
            if (driver.find_element(By.ID,"id_error_q")):
                return True
        else: return False
        
class TestAssignment:
    @staticmethod
    def test(page, assignment, content):
        goToLoginPagesAnd()

        TestUtil.login("student", "moodle")

        input_str = """ page: %s
assignment: %s
content: %s
""" % (
            page,
            assignment,
            content,
        )

        TestUtil.makeSourcePath(input_str, num)
        
        driver.find_element(By.XPATH, "{page}").click()
        driver.find_element(By.XPATH, "{assignment}").click()
        
        if driver.find_elements(By.XPATH, "//button[contains(.,'Add submission')]"):
            driver.find_element(By.XPATH, "//button[contains(.,'Add submission')]").click()
            driver.switch_to.frame(1)
            driver.find_element(By.CSS_SELECTOR, "html").click()
            driver.find_element(By.ID, "tinymce").clear()
            driver.find_element(By.ID, "tinymce").send_keys("{content}")
            driver.find_element(By.ID, "id_submitbutton").click()
            dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
            dest.write("Successfully submit assignment")
            
        elif driver.find_elements(By.XPATH, "//button[contains(.,'Remove submission')]"):
            driver.find_element(By.XPATH, "//button[contains(.,'Remove submission')]").click()
            driver.find_element(By.XPATH, "//button[contains(.,'Continue')]").click()
            dest = open(os.path.join(soldir, str(num) + ".txt"), "w")
            dest.write("Successfully remove submission")
        
        dest = open(os.path.join(SOL_DIR, str(num) + ".txt"), "r")
        line = dest.read()
        return line == expect