from selenium import webdriver
import time

driver = webdriver.Chrome()

url = 'https://telegram.org'
driver.get(url)
time.sleep(1)

# driver.save_screenshot('screenshot.png')

element = driver.find_element_by_tag_name('body')
element_png = element.screenshot_as_png
with open("screenshot2.png", "wb") as file:
    file.write(element_png)

driver.quit()
