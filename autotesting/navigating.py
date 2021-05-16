from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://stackoverflow.com')
time.sleep(1)

driver.get('https://reddit.com')
time.sleep(1)

driver.get('https://github.com')
time.sleep(1)

driver.back()
time.sleep(1)

driver.back()
time.sleep(1)

driver.forward()
time.sleep(1)

time.sleep(4)
driver.quit()

