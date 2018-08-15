import time
from selenium import webdriver
from common.config import  configPage,appurl,apploginname,apppassword
class app_login(configPage):
    usr_loc=("xpath",'//div/input[@type="text"]')
    psw_loc=('xpath','//div/input[@type="password"]')
    button_loc=('xpath','//button[@type="submit"]')

    def login(self,loginname=apploginname,password=apppassword,result=True):
        self.open(appurl)
        self.send_keys(self.usr_loc,loginname)
        self.send_keys(self.psw_loc,password)
        self.click(self.button_loc)
        time.sleep(2)
        # try:
        #     self.click(self.button_loc)
        # except:pass
        # time.sleep(3)
        print(self.get_title())