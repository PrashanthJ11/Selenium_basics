from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get('https://www.flipkart.com/')

#ID and NAME Locators
# driver.find_element(By.NAME,'q').send_keys('laptop under 30000')
# driver.find_element(By.ID,'value').send_keys('value')


#LINKTEXT AND PARTIAL LINK TEXT locators
#driver.find_element(By.LINK_TEXT,'Login').click()
#driver.find_element(By.PARTIAL_LINK_TEXT,'Log').click()

#TagName and Classname
tags=driver.find_elements(By.TAG_NAME,'a')
print(len(tags))
links=driver.find_elements(By.CLASS_NAME,'_2-LWwB')
print(len(links))
driver.maximize_window()
time.sleep(4)


