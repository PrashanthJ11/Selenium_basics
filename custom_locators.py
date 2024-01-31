from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome()
driver.get('https://www.facebook.com/login/')
driver.maximize_window()

# tag and ID
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys('prashanthguru107@gmail.com')
# driver.find_element(By.CSS_SELECTOR,"#email").send_keys('prashanthguru107@gmail.com')

# tag and class
# driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys('prashanthguru107@gmail.com')
# driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys('prashanthguru107@gmail.com')

# tag and attribute
# driver.find_element(By.CSS_SELECTOR,'input[placeholder="Email address or phone number"]').send_keys('prashanth@107hmail.com')
# driver.find_element(By.CSS_SELECTOR,'[placeholder="Email address or phone number"]').send_keys('prashanth@107hmail.com')

# tag,class and attribute
driver.find_element(By.CSS_SELECTOR,'input.inputtext[name="email"]').send_keys('Rishi@107gmail.com')
driver.find_element(By.CSS_SELECTOR,'input.inputtext[name="pass"]').send_keys('Rishi@107')

time.sleep(3)
driver.close()