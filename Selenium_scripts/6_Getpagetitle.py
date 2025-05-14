from selenium import webdriver
import time

# Launch browser
d = webdriver.Chrome()
d.get('https://python.org')
time.sleep(5)

# To Get Window Title
w_title = d.title

print('\n Window title is : ', w_title)
time.sleep(3)

assert w_title == 'Welcome to Python.org' , ' Title is not matched '

time.sleep(10)
d.close()
