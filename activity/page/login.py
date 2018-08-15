#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/24 0024
import time
from selenium import webdriver
from common.config import  configPage,url,loginname,password
class loginPage(configPage):
    usr_loc=("xpath",'//div/input[@type="text"]')
    psw_loc=('xpath','//div/input[@type="password"][2]')
    button_loc=('xpath','//div/input[@type="submit"]')
    tip_loc=('xpath','//*[@id="menu10003202"]')
    # def __init__(self):
    #     self.driver=webdriver.Chrome()
    def input_usr (self,text):
        return  self.send_keys(self.usr_loc,text)
    def input_psw(self,text):
        return  self.send_keys(self.psw_loc,text)
    def click_button(self):
        return  self.click(self.button_loc)
    def get_tip(self):
        t = self.get_text(self.tip_loc)
        return t
    def success(self):
        try:
            result= self.get_tip()
            print(result)
            if result == '首页':
                result = True
                return True
            else:
                return False
        except:
            result = False
            return  result
    def login(self,loginname=loginname,password=password,result=True):
        self.open(url)
        self.input_usr(loginname)
        self.input_psw(password)
        self.click_button()
        time.sleep(2)
        if self.is_exists(self.button_loc):
            self.click_button()
        # except:pass
        # time.sleep(3)
        # print(self.get_title())



if __name__=='__main__':
    webdriver_path=r'D:/PY基础/activity/chromedriver.exe'

    logindriver=loginPage(webdriver.Chrome(executable_path=webdriver_path))

    logindriver.login()
    # time.sleep(3)
    # logindriver.get_url()










