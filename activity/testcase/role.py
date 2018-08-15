from selenium import webdriver
from page.role import rolepage
import unittest
class role(unittest.TestCase):
    def setUp(self):
        self.driver=rolepage(webdriver.Chrome())
        self.driver.login()
    def test_addrole(self):
        self.driver.role()
