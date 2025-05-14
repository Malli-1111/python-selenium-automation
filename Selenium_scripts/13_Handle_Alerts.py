from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

d = webdriver.Chrome()
d.maximize_window()
d.get(r'C:\Users\malli\OneDrive\Desktop\testingpractice\SELENIUM\ALERT.html')
sleep(5)

d.find_element(By.XPATH, '/html/body/button').click()

alert = d.switch_to.alert
sleep(5)

#To accept alert
alert.accept()

#To dismiss alert
alert.dismiss()

#  To get alert message
print(' \n\n ALERT TEXT :: ' , alert.text)
#sleep(5)
sleep(10)
d.close()
