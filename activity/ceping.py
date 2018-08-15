#  /home/pyvip/py_case
#  _*_ coding:utf-8 _*_
# author : yellowsea  time:2018/3/10 0010
from selenium.webdriver.support.wait import  WebDriverWait
from selenium import webdriver
import time,random
gradecode=input('请输入考号:')
password=input('请输入密码:')
print('测评启动中，请稍候...')

driver=webdriver.Chrome()


driver.get('http://api.chinajoinin.com/ceping/10001105.html#/login')
time.sleep(2)
f=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@id="login_two"]/ion-content/div/form/div/div[2]/div/input'))
f.send_keys(gradecode)
f=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@id="login_two"]/ion-content/div/form/div/div[3]/div/input'))
f.send_keys(password)
f=WebDriverWait(driver,5).until(lambda x:x.find_element_by_xpath('//*[@id="login_two"]/ion-content/div/form/div/div[3]/div/input'))
f.submit()#点击登录
time.sleep(2)
f=driver.find_element_by_xpath('//*[@id="rootCtrl"]/body/div[1]/ion-nav-view/div/ion-view/ion-content/div[1]/div/a').text
if f== '已提交':
    print('你已答题完毕')
    f=''
elif  driver.find_element_by_xpath('//*[@id="rootCtrl"]/body/div[1]/ion-nav-view/div/ion-view/ion-content/div[1]/div/a').text == '继续答题':
    print('继续答题')
    driver.find_element_by_tag_name('a').click()
    f=WebDriverWait(driver,5).until(lambda x:x.find_elements_by_class_name('radio-content'))
else:
    print('答题开始')
    driver.find_element_by_tag_name('a').click()
    f=WebDriverWait(driver,5).until(lambda x:x.find_elements_by_class_name('radio-content'))
c=0
while len(f)>0:
    try:

        a = driver.find_element_by_xpath('//*[@id="progress"]/div[2]').text
        b = a.split('/')
        # print(c)
        if c != b[0]:
            print('%s' % b[0])
            c = b[0]
        else:
            # print('第%s题答题中' % b[0])
            c = b[0]

        if len(f) == 5:

                f[random.randint(0, 4)].click()
                f = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_tag_name('button'))
                f.click()
                f = WebDriverWait(driver, 5).until(lambda x: x.find_elements_by_class_name('radio-content'))
        elif len(f) == 2:
            # a=driver.find_element_by_xpath('//*[@id="progress"]/div[2]').text
            # b=a.split('/')
            # if c == b[0]:
            #     print('第%s题答题中' % b[0])
            # else:
            #     print('正在答第%s题'%b[0])
            #     c=int(b[0])+1
                f[random.randint(0, 1)].click()
                f = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_tag_name('button'))
                f.click()
                f = WebDriverWait(driver, 5).until(lambda x: x.find_elements_by_class_name('radio-content'))
        else:
            continue
    except Exception :
        pass
    finally:
        # time.sleep(1)

        if driver.find_element_by_xpath('//*[@id="rootCtrl"]/body/div[1]/ion-nav-view/div/ion-view/ion-content/div[1]/div/div[1]').text=='我的测评结果':
            print('答题结束')
            f=''
        else:
            f = WebDriverWait(driver, 5).until(lambda x: x.find_elements_by_class_name('radio-content'))




