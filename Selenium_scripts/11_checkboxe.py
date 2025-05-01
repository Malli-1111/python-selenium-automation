from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\Users\malli\OneDrive\Desktop\testingpractice\SELENIUM\DROP_DOWN.html')
time.sleep(5)

# Select Check box
obj = driver.find_element(By.ID, 'vehicle2')
obj.click()
time.sleep(5)

driver.find_element(By.ID, 'vehicle3').click()
time.sleep(5)

driver.close()
