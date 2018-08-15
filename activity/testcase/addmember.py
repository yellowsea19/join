import unittest,time
from HTMLTestRunner import HTMLTestRunner

from selenium import webdriver
from page.member import member

class addmember(unittest.TestCase):
    def setUp(self):
        self.driver=member(webdriver.Chrome(r'E:\activity\chromedriver.exe'))
        self.driver.login()

    def tearDown(self):
        self.driver.quit()

    def test_addmember_01(self):
        '''新增人员--学生'''
        self.driver.addmember(loginname='15212341234',user_type=2)

    def test_addmember_02(self):
        '''新增人员--老师'''
        self.driver.addmember(loginname='15212341235',user_type=1)

    def test_delmember_01(self):
        '''删除人员--老师'''
        self.driver.delmember()
    def test_delmember_02(self):
        '''删除人员--学生'''
        self.driver.delmember()

if __name__=='__main__':
    # unittest.main()
    test_dir=r'e:/activity/testcase/'
    discover=unittest.defaultTestLoader.discover(test_dir,pattern='addmember.py')
    now=time.strftime('%Y-%m-%d %H_%M_%S')
    filename=r'E:/activity/report/'+now+'result.html'
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,title='新增人员测试报告',description='测试情况')
    runner.run(discover)
    fp.close()