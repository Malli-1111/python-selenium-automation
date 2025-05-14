# Implicity wait work based on time
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.implicitly_wait(30)

driver.get("http://selenium-python.readthedocs.io")

driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div/ul/li[5]/RRR').click() #dont prefer this xpath realtime 

driver.close()
