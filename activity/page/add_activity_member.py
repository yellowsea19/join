from page.login import loginPage
import time

class Add_activity_member(loginPage):
    activity_guanli=('xpath','//span[text()="活动管理"]')#活动管理
    lunwenzhengji=('xpath','//span[text()="论文征集活动"]')#论文征集
    apply_guanli=('xpath','//tbody/tr[1]/td[10]/a')
    new_member=('xpath','//span[text()="新增"]')
    choose_member=('xpath','//input[@placeholder="请选择报名人"]')


    def add_member(self,school='脚印大学2800',xueyuan='测试学院',zhibu='测试支部'):
        self.click(self.activity_guanli)
        time.sleep(0.5)
        self.click(self.lunwenzhengji)
        time.sleep(0.5)
        self.click(self.apply_guanli)
        time.sleep(1)
        self.click(self.new_member)
        time.sleep(1)
        self.click(self.choose_member)
        time.sleep(0.5)
        self.click(('xpath','//a[text()="%s"]'%school))
        time.sleep(0.5)
        self.click(('xpath','//a[text()="%s"]'%xueyuan))
        time.sleep(1)
        self.click(('xpath','//a[text()="%s"]'%zhibu))
        time.sleep(3)
        self.click(('xpath','//div[text()="20180002"]'))
        self.click(('xpath','//div[text()="20180003"]'))
        self.click(('xpath','//div[text()="20180004"]'))
        time.sleep(0.5)
        self.click(('xpath','//div[@class="modal-footer ng-scope"]/button[text()="确定"]'))
        time.sleep(0.5)
        self.click(('xpath','//input[@value="保存"]'))
        time.sleep(1)
        self.click(('xpath','//div[@class="bootstrap-dialog-footer"]/div/button[text()="确认"]'))



