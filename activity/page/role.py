from page.login import loginPage
from selenium import webdriver
import time
class rolepage(loginPage):
    org=('xpath','//*[@id="menu10000146"]')
    rolebase=('xpath','//*[@id="menu10000162"]')
    new=('xpath','//*[@id="toolbar_btnoption_list"]/div/button[1]')
    lvshu=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[15]/div/div/div[1]/span')
    lvshuchange=('xpath','/html/body/div[1]/div/div/div[2]/div/joinin-group-select/div/ul/li/a')
    button=('xpath','/html/body/div[1]/div/div/div[3]/button[3]')
    rolename=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[16]/div/div/input')
    enrolename=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[17]/div/div/input')
    shujuscope=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[22]/div/div/div[1]/label[2]/span[1]')
    browse=('xpath','//*[@id="10003203_anchor"]/i[1]')
    save=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[29]/div/sf-decorator[1]/div/input')
    savesure=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')




    def role(self,rolename='autotest',enrolename='autotest'):

        self.click(self.org)
        self.click(self.rolebase)
        self.click(self.new)
        self.click(self.lvshu)
        self.click(self.lvshuchange)
        self.click(self.button)
        self.send_keys(self.rolename,rolename)
        self.send_keys(self.enrolename,enrolename)
        self.click(self.shujuscope)
        self.click(self.browse)
        self.click(self.save)
        self.click(self.savesure)










