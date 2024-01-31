#Test cases
# 1.open web browser(chrome/firefox,edge)
# 2.oopen URL https://opensource-demo.orangrhrmlive.com/
# 3.enter username (Admin)
# 4.enter password(admin123)
# 5.click on login
# 6.capture the title of the homepage(actual title)
# 7.verify title of the page :OrangeHRM(expected)
# 8.close browser


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
# driver.get("https://www.facebook.com")
# print(driver.title)
# print(driver.current_url)
# driver.get("https://www.facebook.com/login/")
# print(driver.title)
# print(driver.current_url)


driver=webdriver.Chrome()
driver.get('https://admin-demo.nopcommerce.com/login')

driver.find_element(By.NAME,'Email').clear()
driver.find_element(By.NAME,'Email').send_keys('admin@yourstore.com')
driver.find_element(By.NAME,'Password').clear()
driver.find_element(By.NAME,'Password').send_keys('admin')
driver.find_element(By.CSS_SELECTOR,'.button-1.login-button').click()
act_title=driver.title
exp_title='Your store. Login'
if act_title==exp_title:
    print('test cases are passed')
else:
    print('test failed')
time.sleep(3)
driver.close()




















#
#
#
# print("sample test case started")
# driver = webdriver.Chrome()
# #driver=webdriver.firefox()
# #driver=webdriver.ie()
# #maximize the window size
# driver.maximize_window()
# #navigate to the url
# driver.get("https://www.google.com/")
# #identify the Google search text box and enter the value
# driver.find_element(By.NAME, "q").send_keys("w3schools")
#
# time.sleep(3)
# #click on the Google search button
# driver.find_element(By.NAME,"btnK").click()
# time.sleep(3)
# #close the browser
# driver.close()
# print("sample test case successfully completed")

