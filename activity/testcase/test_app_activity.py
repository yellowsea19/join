from selenium import webdriver
from page.app_login import app_login
from page.activity import idlist
from page.apply_sign_signout import Apply
import unittest,time,datetime,os

class test_app_activity(unittest.TestCase):
    def setUp(self):
        # ospath=os.path.abspath(os.path.join(os.path.dirname('test_01_addactivity.py'),os.path.pardir))
        self.driver=Apply(webdriver.Chrome(r'E:\activity\chromedriver.exe'))

        self.driver.login()


    def tearDown(self):

        self.driver.quit()
    def test_apply(self):
        for id in idlist:
            self.driver.apply(id)