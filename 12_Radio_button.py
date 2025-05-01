from selenium import webdriver
from selenium.webdriver.common.by import By
import time

###  IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()

# Open a URL
driver.get(r'C:\Users\malli\OneDrive\Desktop\testingpractice\SELENIUM\DROP_DOWN.html')
time.sleep(5)


# Select radio button
driver.find_element(By.ID, 'age2').click()

time.sleep(10)
driver.close()
