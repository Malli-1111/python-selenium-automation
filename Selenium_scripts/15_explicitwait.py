from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the Selenium Python docs page
driver.get("http://selenium-python.readthedocs.io")

# Explicit wait: Wait until the desired link or element is present
try:
    # Example: wait for the “FAQ” link to be clickable
    wait = WebDriverWait(driver, 20)
    faq_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "FAQ")))
    faq_link.click()
    print("Successfully clicked the FAQ link.")
except Exception as e:
    print("Error locating or clicking the element:", e)

# Close the browser
driver.quit()
