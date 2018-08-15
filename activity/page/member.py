# from common.config import configPage
import time
from selenium.webdriver.common.keys import Keys
from page import login
class member(login.loginPage):
    oclikc=('xpath','//span[contains(text(),"组织机构管理")]')#组织机构管理
    renyuan=('xpath','//span[contains(text(),"人员信息管理")]')#人员信息管理
    new=('xpath','//span[contains(text(),"新增")]')#新增
    name=('xpath','//input[@placeholder="请输入姓名" and @ng-model="model[\'uuiName\']"]')#姓名
    loginname=('xpath','//input[@placeholder="请输入登录名"]')#登录名
    paw=('xpath','//input[@type="password" and @placeholder="请输入6-12位字符"]')#密码
    paw1=('xpath','//input[@type="password" and @placeholder="请再输入一次"]')#密码确认
    user_student=('xpath','//span[text()="学生"]')#学生类型
    user_teacher=('xpath','//span[text()="教师"]')#老师类型
    org=('xpath','//div[contains(text(),"请选择隶属机构")]')#隶属机构
    keda=('xpath','//a[contains(text(),"科大")]')#选择科大
    sure=('xpath','//div[@class="modal-footer ng-scope"]/button[contains(text(),"确定")]')#确定
    gradecode=('xpath','//input[@placeholder="请输入工号"]')#工号
    student_number=('xpath','//input[@placeholder="请输入学号"]')#学号
    school_system=('xpath','//span[text()="请选择学历类型"]')#请选择学历类型
    zhuanke_three=('xpath','//div[text()="专科三年"]')#专科三年
    zhuanshengben_two=('xpath','//div[text()="专升本二年"]')#专升本二年
    benke_four=('xpath','//div[text()="本科四年"]')#本科四年
    benke_five=('xpath','//div[text()="本科五年"]')#本科五年
    shuoshi_two=('xpath','//div[text()="硕士二年"]')#硕士二年
    shuoshi_three=('xpath','//div[text()="硕士三年"]')#硕士三年
    boshi_two=('xpath','//div[text()="博士二年"]')#博士二年
    boshi_three=('xpath','//div[text()="博士三年"]')#博士三年
    boshi_four=('xpath','//div[text()="博士四年"]')#博士四年
    boshi_five=('xpath','//div[text()="博士五年"]')#博士五年
    uui_code=('xpath','//input[@placeholder="请选择入学时间"]')#请选择入学时间


    role=('xpath','//li/input[@placeholder="请选择"]')
    role1=('xpath','//div[@class="select2-result-label ui-select-choices-row-inner"]/div[text()="普通学生"]')#选择普通学生角色
    save=('xpath','//input[@type="submit"]')#保存
    save1=('xpath','//div/button[@class="btn btn-primary ng-binding"]')#保存确认
    assertelement=('xpath','//tr[1]/td[5]/a/span/text()')

    del_change=('xpath','//tr/td/input[@data-index="0"]')
    delcl=('xpath','//span[text()="删除" ]')
    delsure=('xpath','//button[text()="确认"]')
    rubbish=('xpath','//span[text()="回收站"]' )
    del_change1=('xpath','//input[@data-index="0"]')
    delover=('xpath','//span[text()="彻底删除"]')
    delsure1=('xpath','//button[text()="确认"]')


    def addmember(self,name='autotest',loginname='19800000001',psw='11111111',gradecode='aututest001',user_type=0):
        time.sleep(1)
        self.click(self.oclikc)#点击组织机构管理
        time.sleep(1)
        self.click(self.renyuan)#点击人员信息管理
        time.sleep(1)
        self.click(self.new)#点击新增
        time.sleep(1)
        self.send_keys(self.name,name)#输入姓名
        # a=self.get_attribute(self.name,'value')
        self.send_keys(self.loginname,loginname)#输入用户名手机号码
        self.send_keys(self.paw,psw)#输入密码
        self.send_keys(self.paw1,psw)#输入密码确认

        self.click(self.org)#点击隶属机构
        self.click(self.keda)#选择科大
        self.click(self.sure)#点击确定
        if user_type==0:
            pass
        if user_type==1:
            time.sleep(1)
            self.click(self.user_teacher)
            self.send_keys(self.gradecode,gradecode)#输入工号
        if user_type==2:
            time.sleep(1)
            self.click(self.user_student)#点击学生类型
            time.sleep(1)
            self.click(self.school_system)#点击学历类型
            time.sleep(1)
            self.click(self.benke_five)#选择本科五年
            self.click(self.uui_code)#点击入学时间
            time.sleep(1)
            self.send_keys(self.uui_code,'1')
            time.sleep(2)
            js='document.getElementById("sleEntranceTime").value="2016-09-011"'
            self.js_execute(js)
            self.send_keyboard(self.uui_code,Keys.BACK_SPACE)
            # time.sleep(2000)
            self.send_keys(self.student_number,gradecode)
            # a=self.get_attribute(self.uui_code,'value')
            # print(a)
        self.click(self.role)#点击角色
        time.sleep(2)
        self.click(self.role1)#选择角色
        self.click(self.save)#点击保存
        self.click(self.save1)#保存确认
        time.sleep(2)
        # result=self.find_element(self.assertelement)
        # if loginname==result:
        #     print('新增成功！')




    def delmember(self):
        time.sleep(1)
        self.click(self.oclikc)#点击组织机构管理
        time.sleep(1)
        self.click(self.renyuan)#点击人员信息管理
        time.sleep(2)
        self.click(self.del_change)#选中删除人员
        self.click(self.delcl)#点击删除
        self.click(self.delsure)#确认删除
        time.sleep(2)
        self.click(self.rubbish)#点击回收站
        time.sleep(1)
        self.click(self.del_change)#选择数据
        # self.click(self.del_change)#选择数据
        time.sleep(2)
        self.click(self.delover)#点击彻底删除
        time.sleep(2)
        self.click(self.delsure1)#点击删除确认





