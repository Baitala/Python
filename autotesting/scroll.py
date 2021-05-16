from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://teatrlesi.lviv.ua')
time.sleep(2)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

driver.quit()

