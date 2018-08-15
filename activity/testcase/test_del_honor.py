from page.myhonor import honor
from selenium import webdriver
import unittest,time
class test_honor(unittest.TestCase):
    def setUp(self):
        self.driver=honor(webdriver.Chrome(r'E:\activity\chromedriver.exe'))

        self.driver.login()
        self.driver.addhonor()
    def tearDown(self):
        self.driver.quit()

    def test_delhonor(self):
        '''删除荣誉'''
        self.driver.delhonor()

if __name__=='__main__':
    unittest.main()














