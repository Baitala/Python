from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get('https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_GDP_growth')
time.sleep(1)

table = driver.find_element_by_xpath("//table[@class='wikitable sortable jquery-tablesorter']")

for row in table.find_elements_by_xpath(".//tr"):
    for td in row.find_elements_by_xpath(".//td"):
        print(td.text)
    print("\n")


