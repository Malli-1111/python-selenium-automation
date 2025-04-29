# import webdriver and By class 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Open a Chrome Browser to create driver
driver = webdriver.Chrome()
time.sleep(3)

#To Maximize window
driver.maximize_window()
time.sleep(3)


# Open a URL
driver.get('https://accounts.lambdatest.com/login')
time.sleep(3)

# To enter username in text box based on NAME Locator
uname = driver.find_element(By.NAME, 'email')
uname.send_keys('usermail@gmail.com')
time.sleep(5)

# To enter password in text box based on ID Locator
password = driver.find_element(By.ID, 'password')
password.send_keys('password')
time.sleep(5)

# To click on login button based on XPATH Locator
login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
login_button.click()

# Close a browser
time.sleep(15)
driver.close()


