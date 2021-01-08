from selenium import webdriver
from selenium.webdriver import ActionChains
import XserverTest
import xlwt
import datetime
import random
import xlrd
import time
from  XserverTest.Readexlx import getOnelinedata
from XserverTest.Readexlx import getnrow
worduse = []


Driver = webdriver.Chrome(r'd:\chromedriver.exe')
loginurl = "http://172.17.13.239:12580/"
Driver.get(loginurl)
Driver.maximize_window()


# 登录
def login():
    time.sleep(1)
    login = Driver.find_elements_by_class_name("text.login_content_input")
    login[0].send_keys('admin')
    login[1].send_keys('Bohui@123')
    Driver.find_element_by_class_name('button.bt').click()
    time.sleep(1)
# 找到敏感词管理界面、
def findtab():
    time.sleep(2)
    Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div[4]/ul/li[4]/div[1]').click()
    time.sleep(2)
    Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/nav/ul/li[1]').click()
    print("get")
# 添加一条数据
def  addcard(SensitiveWord , type ):
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div[1]/header/div[2]/button[2]').click()
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/ul/li[1]/input'
                                 ).send_keys(SensitiveWord)
    time.sleep(1)
    Driver.find_element_by_xpath(
        '/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/ul/li[2]/select/option['+ str(type) +']'
                                 ).click()
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div[2]/div[1]/div[2]/div/div/button[1]'
                                 ).click()
    time.sleep(2)


def go():
    line = getnrow()
    print(line)
    for i in range(line):
        word = getOnelinedata(i + 22)
        # word是敏感词处理后的，5是页面上的排序号
        addcard(word, 5)
    print("完成第" + i+22 +"个敏感词添加")

def mainT():
    login()
    findtab()
    go()

mainT()
