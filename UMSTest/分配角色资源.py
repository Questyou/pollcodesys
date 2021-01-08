from selenium import webdriver
import time
import xlwt

OpenURL = 'http://192.168.30.75:11780/ums/login'
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

# 点击下一页：
    Driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[3]/div[2]/ul/li[5]').click()
    time.sleep(1)

def  fenjuese(num):
    user = '/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[2]/div[2]/div/table/tbody/tr['+ str(num)  + ']'
    # 点击选择用户
    print(user)
    Driver.find_element_by_xpath(user).click()
    # 点击分配角色
    Driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li[9]').click()
    time.sleep(1)
    # 点击分配按钮
    Driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/fieldset[2]/table/tbody/tr[4]/td[3]/div[2]').click()
    time.sleep(1)
    # 关闭弹窗
    Driver.find_element_by_xpath('/html/body/div[13]/div[1]/div/div/a[1]').click()
    time.sleep(2)

def fenziyuan():
    # 点击分配资源
    Driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/div[2]/div/div[1]/ul/li[11]').click()
    time.sleep(1)
    #点击前端
    Driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/form/div[1]/ul/li[1]/ul/li/ul/li[1]/ul/li[1]/ul/li[1]/ul/li/ul/li/div/div[8]').click()
    #点击确认按钮
    Driver.find_element_by_xpath('/html/body/div[13]/div[2]/div/form/div[2]/ul/li[1]/div/div').click()
    time.sleep(5)

Login()
for i in range(9):
    fenjuese(i+1)
    fenziyuan()