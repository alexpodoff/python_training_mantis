# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class tmp(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_tmp(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/mantisbt-1.3.4/login_page.php?return=%2Fmantisbt-1.3.4%2Fmanage_proj_page.php")
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username").send_keys("administrator")
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys("secret")
        wd.find_element_by_css_selector("input.button").click()
        wd.find_element_by_link_text("project_name").click()
        self.assertTrue(success)

        wd.find_elements_by_xpath("//div/div[4]/div[2]/table/tbody/tr/td/a")
        wd.find_elements_by_name("pro")
    
    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
