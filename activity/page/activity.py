from page.login import loginPage,url
# from selenium import webdriver
# import requests
from selenium.webdriver.common.keys import Keys

import time,datetime
# name_td=datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m-%d %H:%M')
# td1=datetime.timedelta(hours=1)
# td2=datetime.timedelta(hours=2)
# td3=datetime.timedelta(hours=-1)#自定义签到开始时间差
# newtd1=td1+datetime.datetime.now()
# newtd2=td2+datetime.datetime.now()
# newtd3=td3+datetime.datetime.now()
# dt1=datetime.datetime.strftime(newtd1,'%Y-%m-%d %H:%M')
# dt2=datetime.datetime.strftime(newtd2,'%Y-%m-%d %H:%M')
# dt3=datetime.datetime.strftime(newtd3,'%Y-%m-%d %H:%M')
idlist=[]
# print(dt3)
class activitypage(loginPage):

    all=('xpath','//span[contains(text(),"活动管理") and @ng-bind="menu.name"]')
    all1=('xpath','//span[contains(text(),"全部活动") ]')
    new=('xpath','//span[contains(text(),"新增") ]')#点击新增

    abi_name=('xpath','//input[@placeholder="请输入活动名称"]')#输入活动名称
    unit=('xpath','//div[@placeholder="请选择发布单位"]')#发布单位
    choose_unit=('xpath','//a/div[contains(text(),"345")]')#选择发布单位
    scope=('xpath','//span[contains(text(),"请选择报名范围")]')#点击报名范围
    scope1=('xpath','//div[contains(text(),"科大")]')#选择报名范围
    sponsor=('xpath','//ul/li/input[@placeholder="请选择主办方"]')#点击主办方
    sponsor1=('xpath','//div[contains(text(),"校学生会")]')#选择主办方
    organizer=('xpath','//input[@placeholder="请选择承办方"]')#承办方
    choose_organizer=('xpath','//div[contains(text(),"校学生会")]')
    # abi_type=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[24]/div/div/div[1]/div/div/span')#点击活动类别
    abi_type1=('xpath','//span[contains(text(),"请选择活动类别")]')#点击活动类别
    abi_type2=('xpath','//div[contains(text(),"学术科技类")]')#选择活动类别
    # abi_type3=('xpath','//*[@id="ui-select-choices-row-4-1"]/a/div')

    # target0=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[30]/div/div')
    img=('xpath','//button[contains(text(),"从图片库选择") |@class="btn btn-success picture-lib-btn"]')#点击从图片库选择
    img1=('xpath','//div/div[1]/div/img')#选择图片
    img_sure=('xpath','//div[@class="picture-poppup-footer ng-scope"]/button[@ng-click="save()"]')#点击确定
    intro=('xpath','//div[@class="fr-element fr-view"]')#活动简介
    meaning=('xpath','//div/textarea[@placeholder="请输入活动意义"]')#活动意义
    target1=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[45]/div/label')
    abi_starttime=('xpath','//*[@id="abiStartTime"]')#点击开始时间
    abi_endtime=('xpath','//*[@id="abiEndTime"]')#点击活动结束时间
    # sure=('xpath','/html/body/div[13]/div[3]/div/button[1]')
    shichang=('xpath','//input[@placeholder="请输入活动时长"]')#输入活动时长
    allow=('xpath','//input[@placeholder="请输入允许报名人数"]')#输入报名人数
    sign=('xpath','//select/option[contains(text(),"不需要签到")]')#点击签到模式
    signnomal=('xpath','//select/option[contains(text(),"普通签到")]')#选择普通签到
    signscan=('xpath',' //option[@label="扫描签到"]')#扫描签到
    signadmin=('xpath',' //option[@label="管理员扫描签到"]')#管理员扫描签到
    signticket=('xpath',' //option[@label="验票签到"]')#验票签到
    signout=('xpath',' //option[@label="不需要签退"]')#点击签退
    signoutnomal=('xpath',' //option[@label="普通签退"]')#普通签退
    signoutscan=('xpath',' //option[@label="扫描签退"]')#扫描签退
    signoutadmin=('xpath',' //option[@label="管理员扫描签退"]')#管理员扫描签退
    signoutticket=('xpath',' //option[@label="验票签退"]')#验票签退


    signtime=('xpath','//option[@label="默认（活动开始前15分钟）"]')#点击签到开始时间
    signtime1=('xpath','//option[@label="自定义（在报名开始之后与活动结束之前）"]')#点击自义定签到时间
    signstarttime=('xpath','//input[@placeholder="请选择签到开始时间"]')#自定义签到开始时间
    # customtime=('xpath','//*[@id="signinStartTime"]')#点击自定义时间
    # signbutton=('xpath','/html/body/div[14]/div[3]/div/button[1]')#确定
    # map=('xpath','//span[@class="icon-activities_icon_add1"]')#点击地图
    # maps=('xpath','//span[@ng-if="form.icon"]')
    map=('xpath','//span[@class="icon-activities_icon_add1"]')#点击地图

    mapbutton=('xpath','//div/button[@class="btn btn-success ng-binding ng-scope"]')#点击确定
    target2=('xpath','//*[@id="editformDiv"]/bootstrap-decorator[119]/div/label')#定位
    save=('xpath','//input[@value="保存"]')#点击保存
    save1=('xpath','//button[@class="btn btn-primary ng-binding"]')#确定保存
    a = ('xpath', '//tr[1]/td[3]/a/span')

    # audit_button=('xpath','//div/button[@class="btn btn-success btn-joinpost"]')
    # audit_agree=('xpath','//span[contains(text(),"通过")]')
    # save_button=('xpath','//button[contains(text(),"审核")]')
    # sure_button=('xpath','//button[@class="btn btn-primary ng-binding"]')


    def activity(self,abi_property='普通活动',abi_name='autotest',choose_unit='345',choose_scope='科大',abi_label='学术科技类',abi_label_child='',intro='autotest',meaning='autotest',dt1='dt1',dt2='dt2',shichang='30',allowmember='100',sign=0,signout=0):
        # time.sleep(3)
        # self.click(self.all)#点击活动管理
        # self.click(self.all1)#点击全部活动
        self.click(('xpath','//span[text()="个人中心"]'))#点击个人中心
        time.sleep(0.5)
        self.click(('xpath','//span[text()="我的活动"]'))

        self.click(self.new)#点击新增
        time.sleep(3)
        if self.is_exists(('xpath','//select/option[text()="普通活动"]')):#判断是否区分普通活动和论文征集活动
            self.click(('xpath','//select/option[text()="普通活动"]'))
            self.click(('xpath','//select/option[text()="%s"]'%abi_property))
        self.send_keys(self.abi_name,abi_name)#输入活动名称
        self.click(self.unit)#点击发布单位
        time.sleep(1)
        self.click(('xpath','//a/div[contains(text(),"%s")]'%choose_unit))#选择发布单位
        self.click(self.scope) #点击报名范围
        self.click(('xpath','//div[contains(text(),"%s")]'%choose_scope))#选择报名范围
        self.click(self.sponsor)#点击主办方
        self.click(self.sponsor1)#选择主办方
        self.click(self.organizer)#点击承办方
        self.click(self.choose_organizer)#选择承办方校学生会
        self.click(self.abi_type1)#点击活动类别
        self.click(('xpath','//div[contains(text(),"%s")]'%abi_label))#选择活动类别
        if self.is_exists(('xpath','//span[text()="请选择活动子类别"]')):#判断是否有活动子类别
            self.click(('xpath','//span[text()="请选择活动子类别"]'))#点击活动子类别
            time.sleep(0.5)
            self.click(('xpath','//div[text()="%s"]'%abi_label_child))
        # self.js_focus_element(self.target0)#定位
        self.click(self.img)#点击从图片库选择
        self.click(self.img1)#选择图片
        self.click(self.img_sure)#确定
        self.send_keys(self.intro,intro)#输入简介
        self.send_keys(self.meaning,meaning)#活动意义
        # self.js_focus_element(self.target1)#元素聚焦
        self.click(self.abi_starttime)#点击活动开始时间
        time.sleep(1)
        self.send_keys(self.abi_starttime,'2')#开始时间
        # js='document.getElementById("abiStartTime").value="%s"'%dt1
        # # print(js)
        # self.js_execute(js)
        # time.sleep(5)
        # self.send_keys(self.abi_starttime,Keys.BACK_SPACE)
        # time.sleep(5)
        # self.send_keys(self.abi_starttime,Keys.TAB)
        self.send_keys(self.abi_starttime,'2')#开始时间
        self.send_keys(self.abi_starttime,dt1)
        self.click(self.abi_endtime)
        time.sleep(1)
        # self.send_keys(self.abi_endtime,'2')
        # js='document.getElementById("abiEndTime").value="%s"'%dt2
        # self.js_execute(js)
        # time.sleep(5)
        # self.send_keys(self.abi_endtime,Keys.BACK_SPACE)
        # time.sleep(5)
        # self.send_keys(self.abi_endtime,Keys.TAB)
        self.click(self.abi_endtime) #结束时间
        self.send_keys(self.abi_endtime,'2')

        self.send_keys(self.abi_endtime,dt2)
        # self.send_keys(self.abi_endtime,dt2,is_clear=True)
        time.sleep(1)
        self.click(self.shichang)
        self.send_keys(self.shichang,shichang)#时长
        self.send_keys(self.allow,allowmember)#输入报名人数
        if sign==0:
            pass
        if sign==1:
            self.click(self.sign)
            self.click(self.signnomal)#普通签到

        if sign==2:
            self.click(self.sign)
            self.click(self.signscan)#扫码签到
        if sign==3:
            self.click(self.sign)
            self.click(self.signadmin)#管理员扫码签到
        if sign==4:
            self.click(self.sign)
            self.click(self.signticket)#验票签到
        if signout==0:
            pass #不需要签退
        if signout==1:
            self.click(self.signout)
            self.click(self.signoutnomal)#普通签退
        if signout==2:
            self.click(self.signout)
            self.click(self.signoutscan)#扫描签退
        if signout==3:
            self.click(self.signout)
            self.click(self.signoutadmin)#管理员扫描签退
        if signout==4:
            self.click(self.signout)
            self.click(self.signoutticket)#验票签退
        # self.click(self.map)#点击地图
        self.click(self.map)
        time.sleep(2)
        self.click(self.mapbutton)#点击确定

        if abi_property=='论文征集活动':
            time.sleep(1)
            self.click(('xpath','//div[@placeholder="请选择荣誉类别"]/span'))
            time.sleep(0.5)
            self.click(('xpath','//div[text()="专利证书"]'))
            time.sleep(2)
            f=('xpath','//input[@class="form-control col-width-100 ng-pristine ng-untouched ng-valid"]')
            num_list=self.find_elements(f)
            time.sleep(3)
            # print(num_list)
            # self.send_keys(num_list[1],'5')
            for num in num_list:
                num.send_keys('1')
                time.sleep(1)
            self.click(('xpath','//input[@placeholder="请选择二评人员"]'))
            time.sleep(1)
            self.click(('xpath','//a[text()="脚印大学2800"]'))
            time.sleep(1)
            self.click(('xpath','//a[text()="院系"]'))
            time.sleep(1)
            self.click(('xpath','//div[text()="院系人员"]'))
            time.sleep(1)
            self.click(('xpath','//div[@class="modal-footer ng-scope"]/button[text()="确定"]'))
            time.sleep(1)
            self.send_keys(('xpath','//input[@placeholder="请输入公示周期"]'),'1')
        # self.js_focus_element(self.target2)
        time.sleep(2)
        self.click(self.save)#点击确定
        time.sleep(1)
        self.click(self.save1)#确认保存
        time.sleep(3)
        self.click(self.a)#点击新增的活动进入活动详情
        time.sleep(3)
        addurl=self.get_url()
        id=addurl.split('/')[-1]
        with open('idlist.txt','a+') as f:

            f.write(id+'\n')
            f.close()
        # idlist.append(id)
        # print("id=",id)

    # def audit1(self,id):
    #     print(id)
    #     auditurl=url+'#/activitybaseinfo/edit/show/5/'+id
    #     self.open(auditurl)
    #     self.click(self.audit_button)
    #     self.click(self.audit_agree)
    #     self.click(self.save_button)
    #     self.click(self.sure_button)
    #
    # def audit2(self,id):
    #     auditurl=url+'#/activitybaseinfo/edit/show/7/'+id
    #     self.open(auditurl)
    #     time.sleep(3)
    #     self.click(self.audit_button)
    #     self.click(self.audit_agree)
    #     self.click(self.save_button)
    #     self.click(self.sure_button)
