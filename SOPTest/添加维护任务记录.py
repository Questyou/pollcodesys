from selenium import webdriver
import time
import xlwt

ItemList = ['任务名称a',]
DevList = ['/html/body/div[3]/div[2]/div/div/equip-task/div/div[5]/div[2]/div/device-dir/div/div/div[2]/div/fieldset/fieldset/ul/li[1]/label[1]/input',
           '/html/body/div[3]/div[2]/div/div/equip-task/div/div[5]/div[2]/div/device-dir/div/div/div[2]/div/fieldset/fieldset/ul/li[2]/label[1]/input']
ItemMedo = ['/html/body/div[3]/div[2]/div/div/equip-task/div/div[7]/div[2]/div/ul/li[3]/span[2]/select/option[3]',
            '/html/body/div[3]/div[2]/div/div/equip-task/div/div[7]/div[2]/div/ul/li[3]/span[2]/select/option[2]']
ItemLevel = ['/html/body/div[3]/div[2]/div/div/equip-task/div/div[7]/div[2]/div/ul/li[4]/span[2]/input[3]',
             '/html/body/div[3]/div[2]/div/div/equip-task/div/div[7]/div[2]/div/ul/li[4]/span[2]/input[2]',
             '/html/body/div[3]/div[2]/div/div/equip-task/div/div[7]/div[2]/div/ul/li[4]/span[2]/input[1]']
Driver = webdriver.Chrome(r'd:\chromedriver.exe')
#直接进入了设备维护管理页面
Driver.get('http://172.17.13.92:24680//index.html?token=67eb4e2d-1a38-41f0-928d-4d278853c7e3#/equipDefendManager')
time.sleep(2)
Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/ul/li[2]/a/span/em').click()
time.sleep(1)
for i in range(30):
    #点击添加任务
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/equip-task/div/div[1]/a[1]').click()
    time.sleep(2)
# 设置任务信息
    # 选择设备
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/equip-task/div/div[7]/div[2]/div/ul/li[1]/span[2]/input').click()
    time.sleep(1)
    Driver.find_element_by_xpath(DevList[i % 2]).click()
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/equip-task/div/div[5]/div[3]/a[1]').click()
    # 任务名称
    ItemName = str(ItemList[0]) + str(i)
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/equip-task/div/div[7]/div[2]/div/ul/li[2]/span[2]/input').send_keys(ItemName)
    #任务模板
    Driver.find_element_by_xpath(ItemMedo[i % 2]).click()
    #维护级别
    Driver.find_element_by_xpath(ItemLevel[i % 3]).click()
    time.sleep(1)
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/equip-task/div/div[7]/div[3]/a[1]').click()



