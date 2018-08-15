#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/14 0014
from selenium import webdriver
from page.activity import activitypage
import unittest, time, datetime, os
import ddt

# @ddt.ddt
class test_activity(unittest.TestCase):

    def setUp(self):
        self.name_td = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M')
        self.td1 = datetime.timedelta(hours=1)
        self.td2 = datetime.timedelta(hours=2)
        self.td3 = datetime.timedelta(hours=-1)  # 自定义签到开始时间差
        self.newtd1 = self.td1 + datetime.datetime.now()
        self.newtd2 = self.td2 + datetime.datetime.now()
        self.newtd3 = self.td3 + datetime.datetime.now()
        self.dt1 = datetime.datetime.strftime(self.newtd1, '%Y-%m-%d %H:%M:%S')
        self.dt2 = datetime.datetime.strftime(self.newtd2, '%Y-%m-%d %H:%M:%S')
        self.dt3 = datetime.datetime.strftime(self.newtd3, '%Y-%m-%d %H:%M')
        # ospath = os.path.abspath(os.path.join(os.path.dirname('test_01_addactivity.py'), os.path.pardir))
        self.driver = activitypage(webdriver.Chrome(r'E:\activity\chromedriver.exe'))

        self.driver.login()

    def tearDown(self):
        self.driver.quit()

    # def test_addactivity_01(self):
    #     '''新增不需要签到不需要签退活动'''
    #     self.driver.activity(abi_name=self.name_td+'不需要签到不需要签退' , dt1=self.dt1, dt2=self.dt2)
    # '''abi_property='普通活动',abi_name='autotest',choose_unit='345',choose_scope='科大',abi_label='学术科技类',abi_label_child='',intro='autotest',meaning='autotest',dt1=self.dt1,self.dt2,shichang='30',allowmember='100',sign=0,signout=0'''

    def test_addactivity_001(self):
        '''新增论文征集活动'''
        self.driver.activity(abi_property='论文征集活动',abi_name='论文征集活动'+self.dt1,choose_unit='测试支部',choose_scope='脚印大学2800',abi_label='思想成长类',abi_label_child='思想成长学时',intro='autotest',meaning='autotest',dt1=self.dt1,dt2=self.dt2,shichang='30',allowmember='100',sign=0,signout=0)
    # def test_addactivity_02(self):
    #     '''新增普通签到不需要签退活动'''
    #     self.driver.activity(abi_name=self.name_td+'普通签到不需要签退' , dt1=self.dt1, dt2=self.dt2, sign=1)
    #

    # def test_addactivity_03(self):
    #     '''新增扫描签到不需要签退活动'''
    #     self.driver.activity(abi_name='扫描签到不需要签退' + self.name_td, dt1=self.dt1, dt2=self.dt2, sign=2)
    #
    # #
    # def test_addactivity_04(self):
    #     '''新增管理员扫描签到不需要签退活动'''
    #     self.driver.activity(abi_name='管理员扫描签到不需要签退' + self.name_td, dt1=self.dt1, dt2=self.dt2, sign=3)
    #
    #
    # def test_addactivity_05(self):
    #     '''新增验票签到不需要签退活动'''
    #     self.driver.activity(abi_name='验票签到不需要签退' + self.name_td, dt1=self.dt1, dt2=self.dt2, sign=4)
    #
    # def test_addactivity_06(self):
    #     '''新增不需要签到普通签退活动'''
    #     self.driver.activity(abi_name='不需要签到普通签退' + self.name_td, dt1=self.dt1, dt2=self.dt2, signout=1)
    #
    # def test_addactivity_07(self):
    #     '''新增不需要签到扫描签退活动'''
    #     self.driver.activity(abi_name='不需要签到扫描签退' + self.name_td, dt1=self.dt1, dt2=self.dt2, signout=2)
    #
    # def test_addactivity_08(self):
    #     '''新增不需要签到管理员扫描签退活动'''
    #     self.driver.activity(abi_name='不需要签到管理员扫描签退' + self.name_td, dt1=self.dt1, dt2=self.dt2, signout=3)
    #
    # def test_addactivity_09(self):
    #     '''新增不需要签到验票签退活动'''
    #     self.driver.activity(abi_name='不需要签到验票签退' + self.name_td, dt1=self.dt1, dt2=self.dt2, signout=4)
    #
    # def test_addactivity_10(self):
    #     '''新增普通签到普通签退活动'''
    #     self.driver.activity(abi_name='普通签到普通签退' + self.name_td, dt1=self.dt1, dt2=self.dt2, sign=1, signout=1)

    #
    # @ddt.data(*idlist)
    #
    # def test_audit1(self,idlist):
    #     '''一审活动'''
    #     print('活动ID：'+idlist+'一审中')
    #     # idlist=['1016218719866720519']
    #
    #     self.driver.audit1(idlist)
    #
    # @ddt.data(*idlist)
    # def test_audit2(self,idlist):
    #     self.driver.audit2(idlist)
        # print(idlist)
    #     '''二审活动'''
    #     idlist = ['1017291875230552073', '1017292095154688003', '1017292314747474182', '1017292533191020545',
    #               '1017292751806533890', '1017292970598207491', '1017293189192749064', '1017293411700576517',
    #               '1017293878329479429']
    #
    #     for id in idlist:
    #         try:
    #             self.driver.audit2(id)
    #         except:
    #             pass
if __name__=='__main__':
    unittest.main()
