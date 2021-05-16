# A simple hello world example
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() # do not add anything as param here as it overrides PATH
driver.get("http://www.lipsum.com/feed/html")

time.sleep(2)

element =  driver.find_element_by_xpath('//*[@id="Inner"]/h1')
print(element.text)

driver.quit()
