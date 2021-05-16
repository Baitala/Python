# A simple hello world example
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() # do not add anything as param here as it overrides PATH
driver.get("https://duckduckgo.com/")

time.sleep(2)

searchBox =  driver.find_element_by_xpath('//*[@id="search_form_input_homepage"]')
searchBox.send_keys('teatr lesi')

time.sleep(4)

searchBox.send_keys(Keys.ENTER)

time.sleep(2)


print(element.text)

driver.quit()
