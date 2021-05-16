from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://stackoverflow.com/users/login'
driver.get(url)
time.sleep(1)

emailfield = driver.find_element_by_id('email')
emailfield.send_keys('email@example.com')

passwordfield = driver.find_element_by_id('password')
passwordfield.send_keys('12345')

loginbutton = driver.find_element_by_id('submit-button')
loginbutton.click()

time.sleep(10)
driver.quit()

