from selenium import webdriver
import time

# Launch Chrome browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open Python website
driver.get("https://www.python.org")

# Refresh (reload) the page 3 times with delays
for i in range(3):
    time.sleep(5)  # Wait before refreshing
    print(f"Refreshing {i+1} time(s)...")
    driver.refresh()

# Optional: wait before closing
time.sleep(5)
driver.quit()
