from selenium import webdriver
from common.config import configPage,url
from page import login
from selenium.webdriver.common.keys import Keys
import time

class honor(login.loginPage):
    local_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    #个人中心
    mycenter=('xpath','//span[text()="个人中心"]')
    #我的荣誉
    myhonor=('xpath','//span[text()="我的荣誉"]')
    #新增
    newhonor=('xpath','//span[text()="新增"]')
    #荣誉类型
    honor_type=('xpath','//div/span[@tabindex="-1"]/span[contains(text(),"请选择荣誉类型")]')
    #选择荣誉类型
    other_honor=('xpath','//a/div[contains(text(),"其它类型")]')
    activity_honor=('xpath','//a/div[contains(text(),"活动类型")]')
    #荣誉类别
    honor_sort=('xpath','//div/span[@tabindex="-1"]/span[contains(text(),"请选择荣誉类别")]')
    #荣誉子类别

    #发表平台
    pingtai=('xpath','//input[@placeholder="请输入发表平台"]')
    #等级记录
    level=('xpath','//input[@placeholder="请输入等级记录"]')
    #校内职务
    xiaoneizhiwu_sort=('xpath','//a/div[contains(text(),"校内职务")]')
    #作品名称
    title_name=('xpath','//input[@placeholder="请输入作品名称"]')
    #荣誉名称
    honor_name=('xpath','//div[@class="joininputcol"]/input[@placeholder="请输入荣誉名称"]')
    #获取时间
    honor_starttime=('xpath','//input[@placeholder="请选择开始时间"]')
    honor_endtime=('xpath','//input[@placeholder="请选择结束时间"]')
    get_date=('xpath','//input[@placeholder="请选择获取时间"]')
    #荣誉介绍
    Description=('xpath','//textarea[@id="uhiDescription"]')
    #审核机构
    audit_org=('xpath','//div[text()="请选择审核机构"]')
    #机构名称：院系
    yuanxi_org=('xpath','//a[text()="院系"]')
    #确定
    org_sure=('xpath','//div[@class="modal-footer ng-scope"]/button[text()="确定"]')
    #审核人员
    audit_member=('xpath','//span[text()="请选择审核人员"]')
    #院系人员
    yuanxi_member=('xpath','//div[text()="院系人员"]')


    #保存
    save=('xpath','//input[@type="submit"]')
    #保存确认
    savesure=('xpath','//button[@class="btn btn-primary ng-binding"]')

    #资质管理
    zizhi_manage=('xpath','//span[text()="资质管理"]')
    #荣誉管理
    honor_manage=('xpath','//span[text()="荣誉管理"]')
    #选择列表第一条数据
    firt_data=('xpath','//input[@data-index="0"]')
    #删除
    delete=('xpath','//span[text()="删除"]')
    #确认删除
    del_sure=('xpath','//div[@class="bootstrap-dialog-footer-buttons"]/button[text()="确认"]')
    #回收站
    trash=('xpath','//span[text()="回收站"]')
    #彻底删除
    pack=('xpath','//span[text()="彻底删除"]')
    #删除恢复
    recover=('xpath','//span[text()="还原数据"]')
    def honor_sort_choose(self,sort_name='校内职务'):
        sort=('xpath','//a/div[contains(text(),{})]'.format(sort_name))
        return sort


    def addhonor(self,sort='校内职务',sort_child='校级-Ⅰ类',title_name=local_time,honorname='test_'+local_time,Description='简介测试',audit_yuanxi='院系',audit_member='院系人员'):
        self.click(self.mycenter)#点击个人中心
        self.click(self.myhonor)#点击我的荣誉
        time.sleep(1)
        self.click(self.newhonor)#点击新增
        self.click(self.honor_type)#点击荣誉类型
        self.click(self.other_honor)#选择其它荣誉
        self.click(self.honor_sort)#点击荣誉类别

        time.sleep(1)
        self.click(('xpath','//a/div[text()="%s"]'%sort))#选择荣誉类别

        if sort=='工作履历':
            self.click(('xpath','//span[text()="请选择荣誉子类别"]'))
            time.sleep(1)
            self.click(('xpath','//a/div[text()="%s"]'%sort_child))
            self.send_keys(('xpath','//input[@placeholder="请输入职务名称"]'),'学生会')
        if sort=='荣誉奖励' or sort=='竞赛获奖'or sort=='论文著作' or sort=='各类证书':
            self.click(('xpath','//span[text()="请选择荣誉子类别"]'))
            time.sleep(1)
            self.click(('xpath','//a/div[text()="%s"]'%sort_child))
        if self.is_exists(self.level):
            self.send_keys(self.level,'一级')
        if self.is_exists(self.pingtai):
            self.send_keys(self.pingtai,'活动管理平台')
        if self.is_exists(self.honor_starttime): #判断是否有开始时间
            self.click(self.honor_starttime)#荣誉开始时间
            js='document.getElementById("uhiDateStart").value="2016-09-011"'
            self.js_execute(js)
            self.send_keyboard(self.honor_starttime,Keys.BACK_SPACE)
            self.click(self.honor_endtime)#结束时间
            js='document.getElementById("uhiDateEnd").value="2017-09-011"'
            self.js_execute(js)
            self.send_keyboard(self.honor_endtime,Keys.BACK_SPACE)
            self.send_keyboard(self.honor_endtime,Keys.TAB)
        if self.is_exists(self.title_name):
            self.send_keys(self.title_name,title_name)#作品名称

        self.send_keys(self.honor_name,honorname)#荣誉名称

        if self.is_exists(self.get_date):#获取时间
            self.click(self.get_date)
            js='document.getElementById("uhiDateStart").value="2017-09-011"'
            self.js_execute(js)
            time.sleep(0.5)
            self.send_keyboard(self.get_date,Keys.BACK_SPACE)
            time.sleep(0.5)
            self.send_keyboard(self.get_date,Keys.TAB)

        self.send_keys(self.Description,Description)#荣誉简介
        time.sleep(3)
        if self.is_exists(self.audit_org):#判断是否是指定人审核
            time.sleep(1)
            self.click(self.audit_org)
            time.sleep(1)
            self.click(('xpath','//a[text()="%s"]'%audit_yuanxi))#选择审核机构
            self.click(self.org_sure)
            time.sleep(1)
            self.click(self.audit_member)
            self.click(('xpath','//div[text()="%s"]'%audit_member))#选择审核人员

        self.click(self.save)#点击保存
        self.click(self.savesure)#确认提交
        time.sleep(5)


    def delhonor(self):
        time.sleep(1)
        self.click(self.zizhi_manage)
        time.sleep(1)
        self.click(self.honor_manage)
        self.click(self.firt_data)
        self.click(self.delete)
        time.sleep(1)
        self.click(self.del_sure)
        time.sleep(1)
        self.click(self.trash)
        time.sleep(1)
        self.click(self.firt_data)
        self.click(self.pack)
        time.sleep(1)
        self.click(self.del_sure)
































