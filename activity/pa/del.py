from selenium import webdriver
import time


driver=webdriver.Chrome()
driver.maximize_window()
driver.get('http://xdnl.xidian.edu.cn/public#/login')
driver.find_element_by_xpath('//*[@id="ngform"]/bootstrap-decorator[1]/div/div/input').send_keys('13111111111')
driver.find_element_by_xpath('//*[@id="ngform"]/bootstrap-decorator[2]/div/input[2]').send_keys('Jy123456')
driver.find_element_by_xpath('//*[@id="ngform"]/bootstrap-decorator[4]/div/input').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="ngform"]/bootstrap-decorator[4]/div/input').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="menu10000146"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="menu10000169"]').click()
time.sleep(2)



time.sleep(1)
for i in range(10):
    driver.find_element_by_xpath('//*[@id="ngform"]/div[2]/bootstrap-decorator[2]/div/table/tbody/tr[2]/td[1]/a/i').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ngform"]/div[2]/bootstrap-decorator[2]/div/table/tbody/tr[3]/td[1]/a/i').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="ngform"]/div[2]/bootstrap-decorator[2]/div/table/tbody/tr[3]/td[1]/a/i').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="toolbar_btnoption_list"]/button[3]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div[8]/div/div/div[3]/div/div/button[2]').click()
    time.sleep(1)