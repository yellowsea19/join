from selenium import webdriver
from page.add_activity_member import Add_activity_member
import unittest, time, datetime, os

class audit_activity(unittest.TestCase):

    def setUp(self):
        self.driver=Add_activity_member(webdriver.Chrome(r'E:\activity\chromedriver.exe'))
        self.driver.login()

    def tearDown(self):
        self.driver.quit()

    def test_001(self):
        self.driver.add_member()