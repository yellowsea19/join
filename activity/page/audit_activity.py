from page.login import loginPage,url
import time


class audit_activity_page(loginPage):
    audit_button=('xpath','//div/button[@class="btn btn-success btn-joinpost"]')
    audit_agree=('xpath','//span[contains(text(),"通过")]')
    save_button=('xpath','//button[contains(text(),"审核")]')
    sure_button=('xpath','//button[@class="btn btn-primary ng-binding"]')



    def audit1(self,id):
        print(id)
        auditurl=url+'#/activitybaseinfo/edit/show/5/'+id
        self.open(auditurl)
        self.click(self.audit_button)
        self.click(self.audit_agree)
        self.click(self.save_button)
        self.click(self.sure_button)

    def audit2(self,id):
        auditurl=url+'#/activitybaseinfo/edit/show/7/'+id
        self.open(auditurl)
        time.sleep(3)
        self.click(self.audit_button)
        self.click(self.audit_agree)
        self.click(self.save_button)
        self.click(self.sure_button)

