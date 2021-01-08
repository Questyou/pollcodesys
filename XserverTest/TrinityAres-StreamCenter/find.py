from selenium import webdriver
import time
import xlwt
from selenium.webdriver import  ActionChains
from XserverTest import  Readexlx
import xlrd
import re

Driver = webdriver.Chrome(r'd:\chromedriver.exe')
url = 'http://172.17.13.98:10009/'

Driver.get(url)

time.sleep(3)
#获取菜单列表
menus = Driver.find_elements_by_class_name("menuItem")

menus[1].click()

time.sleep(1)

Readexlx.getnrow()

#读取SC待添加的流
def readfile():
    print('等待读取SC待添加的文件')



#添加SC任务
def addwork(self, progcode, progname, progurl):
#点击添加按钮
    Driver.find_element_by_css_selector('[class="blue_button add"]').click()
    time.sleep(2)

    Driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div[1]/span[2]/input').send_keys("Pro1")
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div/div/div[2]/div/div[3]/div[2]/div[2]/span[2]/input').send_keys("节目1")
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div[3]/div[2]/div[4]/span[2]/input').send_keys('http://172.17.13.46:10080/realtime/1_195000_11')
    #选择录像
    Driver.find_element_by_css_selector('[class="el-switch el-switch--wide"]').click()

    #点击确认添加
    Driver.find_element_by_css_selector('[class="blue_button sure"]').click()


