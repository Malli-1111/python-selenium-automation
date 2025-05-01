from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# IF driver in current path ###
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(r'C:\Users\malli\OneDrive\Desktop\testingpractice\SELENIUM\DROP_DOWN.html')
time.sleep(5)

drop_element = driver.find_element(By.ID, 'MONTHS')

months = Select(drop_element)

time.sleep(5)

## To select a value based on visable text
months.select_by_visible_text('April')
time.sleep(5)

## To select a value based on value
months.select_by_value('Feb')


## To select a value based on index
months.select_by_index(4)

time.sleep(10)
driver.close()   
