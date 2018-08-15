from selenium import webdriver
from common.config import configPage
import time

class Weibo:
    def __init__(self):
        self.driver=configPage(webdriver.Chrome())
        self.user_name=('xpath','//div[@class="joininputcol"]/input')
        self.psw=('xpath','//div/input[@type="password"][2]')
        self.bottom=('xpath','//div/input[@type="submit"]')

    def login(self,username,password):
        url='http://10.0.0.223:8001/public#/login'
        self.driver.open(url)
        self.driver.max_window()
        self.driver.find_element(self.user_name).send_keys(username)
        self.driver.find_element(self.psw).send_keys(password)
        self.driver.find_element(self.bottom).click()
        time.sleep(3)
        print(self.driver.get_title())
        assert  '后台管理系统' in  self.driver.get_title()
        self.driver.quit()


if __name__=='__main__':

    weibo=Weibo()
    weibo.login('13111111111','11111111')

