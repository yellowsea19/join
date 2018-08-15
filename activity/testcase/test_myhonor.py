from page.myhonor import honor
from selenium import webdriver
import unittest,time
class test_honor(unittest.TestCase):
    def setUp(self):
        self.driver=honor(webdriver.Chrome(r'E:\activity\chromedriver.exe'))

        self.driver.login(loginname=19920180001,password='11111111')

    def tearDown(self):
        self.driver.quit()


    # def test_addhonor_01(self):
    #     '''新增荣誉-校内职务'''
    #     self.driver.addhonor(Description='99')

    def test_addhonor_02(self):
        '''新增荣誉-工作履历'''
        self.driver.addhonor(sort='工作履历',sort_child='校级-Ⅰ类',audit_yuanxi='校团委',audit_member='秀梅')
    def test_addhonor_03(self):
        '''新增荣誉-荣誉奖励'''
        self.driver.addhonor(sort='荣誉奖励',sort_child='国家级-Ⅰ类',audit_yuanxi='校团委',audit_member='秀梅')

    def test_addhonor_04(self):
        '''新增荣誉-竞赛获奖'''
        self.driver.addhonor(sort='竞赛获奖',sort_child='国家级-Ⅰ类',audit_yuanxi='校团委',audit_member='秀梅')
    def test_addhonor_05(self):
        '''新增荣誉-论文著作'''
        self.driver.addhonor(sort='论文著作',sort_child='学术论文-Ⅰ类',audit_yuanxi='校团委',audit_member='秀梅')

    def test_addhonor_06(self):
        '''新增荣誉-各类证书'''
        self.driver.addhonor(sort='各类证书',sort_child='专利证书-Ⅰ类',audit_yuanxi='校团委',audit_member='秀梅')


    def test_delhonor(self):
        '''删除荣誉'''
        self.driver.delhonor()

if __name__=='__main__':
    unittest.main()














