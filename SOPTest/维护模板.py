from selenium import webdriver
import time

import xlwt

OpenURL = 'http://172.17.13.92:24680//index.html?token=49309f42-3721-4a49-a061-b96cc7affd1e#/equipDefendManager'

Driver = webdriver.Chrome(r'd:\chromedriver.exe')
#直接进入了设备维护页面
Driver.get(OpenURL)
Driver.maximize_window()
time.sleep(1)
#add  matacnce modo  目的是输入一个模板的信息，批量生产多个模板
def addmodo(name , level, period):
    addmodobtn =  Driver.find_elements_by_class_name('operation_a')
    addmodobtn[0].click()
    time.sleep(1)
    Driver.find_element_by_class_name("[class='text ng-pristine ng-valid ng-empty ng-touched']").send_keys(name)
    modolevel = Driver.find_elements_by_class_name("[class='radio ng-valid ng-not-empty ng-dirty ng-touched']")
    modolevel[level].click()
    # if period ==
addmodo()