from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://selenium-python.readthedocs.io/")
time.sleep(5)

driver.execute_script("document.body.style.zoom='300%'")
time.sleep(10)
driver.execute_script("document.body.style.zoom='100%'")
time.sleep(10)
driver.close()
