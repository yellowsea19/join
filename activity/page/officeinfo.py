from  page.login import loginPage
import time
class officeinfopage(loginPage):
    orgmenu=('xpath','//*[@id="menu10000146"]')
    officeinfomenu=('xpath','//*[@id="menu10000169"]')
    new=('xpath','//*[@id="toolbar_btnoption_list"]/button[1]')
    office=('xpath','//*[@id="10000002"]/div')
    fullname=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[5]/div/div/input')
    shortname=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[6]/div/div/input')
    yuanxi=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[8]/div/div/div[1]/label[1]/span[1]')
    shetuanlianmeng=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[8]/div/div/div[1]/label[2]/span[1]')
    zhishu=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[8]/div/div/div[1]/label[3]/span[1]')
    save=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[22]/div/sf-decorator[1]/div/input')
    savesure=('xpath','/html/body/div[8]/div/div/div[3]/div/div/button[2]')
    t=('xpath','//*[@id="ngform"]/div[2]/bootstrap-decorator[2]/div/table/tbody/tr[1]/td[1]/span')
    def addofficeinfo(self,fullname='autotest',shortname='autotest'):
        self.click(self.orgmenu)
        self.click(self.officeinfomenu)#点击下级机构
        time.sleep(3)
        self.click(self.new)#点击新增
        self.click(self.office)#选择机构
        self.send_keys(self.fullname,fullname)#输入全称
        self.send_keys(self.shortname,shortname)#输入简称
        self.click(self.yuanxi)#点击院系
        self.click(self.save)#点击保存
        self.click(self.savesure)#点击确认
        time.sleep(5)
        f=self.get_text(self.t)
        print(f)
