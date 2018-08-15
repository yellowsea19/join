from selenium.common.exceptions import TimeoutException

from common.config import appurl
from page.app_login import app_login
import time,datetime

class Apply(app_login):
    button=('xpath','//button[@ng-click="gotoActivityConfirm(0)"]')
    sure=('xpath','//div[@class="acf-but joinin themecolor imbgcolor"]')
    succes=('xpath','//div[@style="margin-top: 10px; text-align: center;"]/p[@class="ng-binding"]')
    go_to_sign=('xpath','//button[@ng-click="gotoActivityConfirm(1)"]')
    go_to_scan=('xpath','//button[contains(text(),"扫码签到")]')
    sure_scan=('xpath','//div[contains(text(),"确认签到")]')
    signflase=('xpath','//p[@style="text-align: center;margin-top:20px"]')
    qrcode=('xpath','//div/button[contains(text(),"签到二维码")]')
    signtiket=('xpath','//div/button[contains(text(),"验票签到")]')
    tiketbutton=('xpath','//div[@class="confirm"]')
    tiketbutton_sure=('xpath','//button[contains(text(),"确定")]')
    tiket_result=('xpath','//div/p[@style="font-size: 16px;margin-top:-20px"]')
    returntext=('xpath','//div/span[@class="ht-info-text"]')
    def apply(self,id):
        url=appurl+'#/activity_details/'+id
        self.open(url)
        time.sleep(2)
        status=self.find_element(self.button).text
        print('当前状态为：'+status)
        time.sleep(1)
        if status=='已结束':
            print(id+':活动状态已结束')

        if status=='马上报名':
            self.click(self.button)
            time.sleep(1)
            self.click(self.sure)
            print(self.find_element(self.succes).text)
            self.apply(id)

        if status=='已报名':


            if self.is_exists(self.go_to_sign,):#判断马上签到是否存在

                self.click(self.go_to_sign)
                self.click(self.sure)
                time.sleep(2)
                text=self.find_element(self.returntext).text
                print('签到结果：'+text)
            if self.is_exists(self.go_to_scan): #判断扫码签到按钮是否存在
                print('扫码签到按钮出现了')
                tmp_url='#/activity_confirm/%s/1/'%id
                scanurl=appurl+tmp_url
                print(scanurl)
                self.open(scanurl)
                self.click(self.sure_scan)
                time.sleep(1)
                text=self.find_element(self.returntext).text
                print('签到结果：'+text)
            if self.is_exists(self.qrcode):
                print('签到二维码出现了')
                tmp_url='#/activity_confirm/%s/1/'%id
                scanurl=appurl+tmp_url
                print(scanurl)
                self.open(scanurl)
                self.click(self.sure_scan)
                time.sleep(2)
                text=self.find_element(self.returntext).text
                print('签到结果：'+text)
            if self.is_exists(self.signtiket):
                self.click(self.signtiket)
                self.click(self.tiketbutton)
                time.sleep(1)
                self.click(self.tiketbutton_sure)
                time.sleep(1)

                result=self.find_element(self.returntext).text
                print(result)
                if self.is_exists(self.tiket_result):

                    print('签到成功')
                elif self.is_exists(self.signflase):
                    print('签到失败')
                else:print('未知错误')

            else:
                print('over')














