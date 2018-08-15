from selenium import webdriver
from page.officeinfo import officeinfopage
import unittest,time
class test_officeinfo(unittest.TestCase):
    def setUp(self):
        self.driver=officeinfopage(webdriver.Chrome())
        self.driver.login()
    def test_addofficeinfo(self):
        '''新增院系'''
        self.driver.addofficeinfo()