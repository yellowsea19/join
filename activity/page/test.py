from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
from selenium.webdriver.common.action_chains import ActionChains
url='http://admin2.join-inapp.com/app_v1/#/login'
driver.implicitly_wait(10)
driver.maximize_window()
time.sleep(2)
driver.get(url)
#打开F12
builder = ActionChains(driver)
builder.key_down(Keys.F12).perform()
time.sleep(1)

dragger1= driver.find_element_by_xpath('//*[@id="login_two"]/ion-content/div[3]/div[1]/ion-slide[1]') # 被拖拽元素

action = ActionChains(driver)

action.click_and_hold(dragger1).move_by_offset(-400, 0).release().perform()
time.sleep(1)
dragger2=driver.find_element_by_xpath('//*[@id="login_two"]/ion-content/div[3]/div[1]/ion-slide[2]/div')
action.click_and_hold(dragger2).move_by_offset(-400, 0).release().perform()
time.sleep(1)
dragger3=driver.find_element_by_xpath('//*[@id="login_two"]/ion-content/div[3]/div[1]/ion-slide[3]/div')
action.click_and_hold(dragger3).move_by_offset(-400, 0).release().perform()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="login_two"]/ion-content/div[3]/div[1]/ion-slide[4]/div[2]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="login_two"]/ion-content/div/form/div/div[2]/div/input').send_keys('13011116666')
driver.find_element_by_xpath('//*[@id="login_two"]/ion-content/div/form/div/div[3]/div/input').send_keys('11111111')
driver.find_element_by_xpath('//*[@id="login_two"]/ion-content/div/form/div/div[4]/div/button').click()


driver.find_element_by_xpath('//*[@id="rootCtrl"]/body/div[5]/div/div[3]/button[2]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="home-ion-cont"]/div/div[4]/div/div/div/div[1]/img').click()
driver.get('http://admin2.join-inapp.com/app_v1/#/activity_details/989697497377153031')
time.sleep(3)
driver.find_element_by_xpath('//*[@id="activity_details"]/div/div[2]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="activity_confirm"]/div/div').click()

f=driver.find_element_by_xpath('//*[@id="activity_result"]/ion-content/div/div[1]/p')
# g=f.get_attribute()
# print(g)