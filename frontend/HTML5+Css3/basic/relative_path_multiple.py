from selenium import webdriver 
from time import sleep
from selenium.webdriver.common.by import By

d = webdriver.Firefox()

d.get("file:///Users/qiqili/Desktop/MySQL%20video/Exercises%20/multiple%20choice.html")

#定义变量存储数据
#data_name = "Sam"
#data_passwd = "123456"

#relative path
hobby1 = d.find_element_by_xpath('//input[@checked]')
hobby2 = d.find_element_by_xpath('//input[2]')
hobby3 = d.find_element_by_xpath('//input[@id="hobby3"]')

hobby3.click()
hobby2.click()


sleep(2)
d.quit()