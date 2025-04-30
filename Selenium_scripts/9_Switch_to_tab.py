from selenium import webdriver
import time

# Open chrome browswer
d = webdriver.Chrome()
d.maximize_window()
d.get("https://www.python.org/")
time.sleep(5)

#Open a new tab with given URL
d.execute_script("window.open('http://robotframework.org/')")
time.sleep(5)

#To get all windows tabs
windows = d.window_handles
print('\n windows ::  ', windows)

print('\n Default tab title :: ', d.title)
time.sleep(5)

#Switch into first tab from right side 
d.switch_to.window(windows[1])
time.sleep(5)
print('\n windows[1] title is :: ', d.title)

#Switch into first tab(Default tab) from left side
d.switch_to.window(windows[0])
time.sleep(5)
print('\n windows[0] title is :: ', d.title)
time.sleep(10)
d.quit()
