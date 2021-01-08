from selenium import webdriver
import time
import xlwt

OpenURL = 'http://172.17.13.76:11780/ums/login'
Driver = webdriver.Chrome(r'd:\chromedriver.exe')
#直接进入了UMS
Driver.get(OpenURL)
time.sleep(2)
def Login():
    Driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form[1]/div/p[1]/input').send_keys('admin')
    Driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form[1]/div/p[2]/input').send_keys('Bohui@123')
    Driver.find_element_by_xpath('/html/body/div/div[2]/div[1]/form[1]/div/div/input').click()
    time.sleep(3)
    Driver.find_element_by_xpath('/html/body/div/ul/li[1]/a').click()
    time.sleep(2)
    Driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[2]/ul/li[1]/div/a').click()
    time.sleep(2)
Login()






