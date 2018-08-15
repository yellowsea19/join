from selenium import webdriver
import time
driver=webdriver.Chrome(r'D:/PY基础/activity/chromedriver.exe')
driver.get('https://www.baidu.com')
time.sleep(3)
print(driver.current_url)
driver.quit()
