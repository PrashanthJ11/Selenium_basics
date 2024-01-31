from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome()
driver.get('https://www.flipkart.com/')
driver.maximize_window()
#Relative x-path
driver.find_element(By.XPATH,'//input[@placeholder="Search for Products, Brands and More"]').send_keys('Laptop')
time.sleep(2)
driver.find_element(By.XPATH,"//button[@title='Search for Products, Brands and More']").click()
time.sleep(4)
