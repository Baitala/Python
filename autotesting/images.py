from selenium import webdriver
import time
import os

driver = webdriver.Chrome()
driver.get('https://teatrlesi.lviv.ua')

time.sleep(2)

images = driver.find_elements_by_tag_name('img')
for image in images:
    imgsrc = image.get_attribute('src')
    os.system("wget " + imgsrc + " .P img")

driver.quit()

