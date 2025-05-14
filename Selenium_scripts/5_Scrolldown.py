# Using execute_script we can run java script
from selenium import webdriver
import time

# Open a Chrome Browser
d = webdriver.Chrome()
d.maximize_window()
d.get("https://www.python.org/")
time.sleep(10)

# To Scroll down page
d.execute_script("window.scrollTo(0, 800)")
time.sleep(10)

# To Scroll up page
d.execute_script("window.scrollTo(0, -800)")
time.sleep(5)

# To Scroll down page bottom
d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)

# Scroll Until an Element is in View
element = driver.find_element(By.ID, "footer")
driver.execute_script("arguments[0].scrollIntoView(true);", element)

d.close()

# Scrolling Type	          JavaScriptExecutor Code
# Scroll Down by Pixels   	window.scrollBy(0, 500);
# Scroll Up by Pixels	      window.scrollBy(0, -500);
# Scroll to Element	        arguments[0].scrollIntoView(true);
# Scroll to Bottom	        window.scrollTo(0, document.body.scrollHeight);
# Scroll to Top           	window.scrollTo(0, 0);
# Scroll Horizontally      	window.scrollBy(200, 0);
# Scroll by Coordinates   	window.scrollTo(100, 400);
