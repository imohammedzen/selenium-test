from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get("https://github.com")
search_field = driver.find_element_by_name('q')
search_field.send_keys("selenium")
search_field.send_keys(Keys.RETURN)
print("waiting 30 mins before doing assertion")
time.sleep(30)
assert "repository results" in driver.page_source
driver.close()
