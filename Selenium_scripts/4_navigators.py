from selenium import webdriver               # Import Selenium's WebDriver for browser automation
from selenium.webdriver.common.by import By  # Import the By class for locating elements
import time                                  # Import time module to use sleep() for waits

# Initialize the Chrome browser
driver = webdriver.Chrome()

# Maximize the browser window
driver.maximize_window()

# Open the official Python website
driver.get("https://www.python.org")

# Wait for 5 seconds to allow the page to load
time.sleep(5)

# Click on the third item in the top navigation bar (Downloads link)
driver.find_element(By.XPATH, '//*[@id="top"]/nav/ul/li[3]/a').click()

# Wait 5 seconds after clicking (let the new page load)
time.sleep(5)

# Navigate back to the previous page
driver.back()

# Wait 5 seconds after going back
time.sleep(5)

# Navigate forward to the next page
driver.forward()

# Wait 5 seconds after going forward
time.sleep(5)

# Close the browser
driver.close()
