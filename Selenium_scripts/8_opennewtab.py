from selenium import webdriver
import time
d = webdriver.Chrome()
d.maximize_window()
d.get("https://www.python.org/")
time.sleep(5)

## Open a new tab with URL
d.execute_script("window.open('https://robotframework.org/')")
time.sleep(10)

## Open a new tab without URL
d.execute_script("window.open()")
time.sleep(10)

# To close only one window(Current)
d.close()

# TO close all tabs 
d.quit()







