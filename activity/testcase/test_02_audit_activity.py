import unittest
from selenium import webdriver
import ddt
from page.audit_activity import audit_activity_page
from testcase.activity_id import  read_idlist
@ddt.ddt
class audit_activity(unittest.TestCase):
    listid=read_idlist()
    def setUp(self):
        self.driver=audit_activity_page(webdriver.Chrome(r'E:\activity\chromedriver.exe'))
        self.driver.login()

    def tearDown(self):
        self.driver.quit()

    @ddt.data(*listid)
    def test_audit1(self,id):
        self.driver.audit1(id)

    @ddt.data(*listid)
    def test_audit2(self,id):
        self.driver.audit2(id)

if __name__=='__main__':
    unittest.main()