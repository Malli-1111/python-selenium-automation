from selenium import webdriver  # Used to control the browser
import time                     # Used to pause the script

                        # Create an instance of Chrome WebDriver
d = webdriver.Chrome()  # Launch Chrome browser

# Maximize the browser window
d.maximize_window()  # Ensure full view of the website for screenshot

# Open the Python official website
d.get('https://www.python.org')  # Navigate to the specified URL

# Wait for 5 seconds to allow page to fully load
time.sleep(5)  # Deliberate wait (can be replaced with explicit waits for better practice)

# Take a screenshot and save it to the specified location
d.save_screenshot(r'C:\Users\malli\OneDrive\Desktop\testingpractice\SELENIUM\malli.png')  # Save screenshot as PNG file (full page)

#This captures only the specific element, not the entire page.

# Locate the element
element = driver.find_element(By.ID, "logo")

# Capture screenshot of the element
element.screenshot("element_screenshot.png")

# Close the browser
d.close()  # Close the browser window
