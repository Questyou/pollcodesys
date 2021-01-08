from selenium import webdriver
import time
import xlwt

OpenURL = 'http://172.17.13.92:24680//index.html?token=b61039a8-3f00-4318-b70c-83994a1e19ba#/equipDefendRecord'

DevList = ['/html/body/div[3]/div[2]/div/div[4]/div[2]/div/device-dir/div/div/div[2]/div/fieldset/fieldset[2]/ul/li[1]/label[2]/input',
           '/html/body/div[3]/div[2]/div/div[4]/div[2]/div/device-dir/div/div/div[2]/div/fieldset/fieldset[2]/ul/li[2]/label[2]/input']
ContantList =['Maintenancetest2']

Driver = webdriver.Chrome(r'd:\chromedriver.exe')
#直接进入了设备维护管理页面
Driver.get(OpenURL)
time.sleep(2)

for i in range(3):
    #点击添加记录
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/a[1]').click()
    time.sleep(1)
    # 设置任务信息
        # 选择设备，把设备的完整路径填写在这里，
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[5]/div[2]/div/ul/li[1]/span[2]/input').click()
        # #交替选择设备；
    time.sleep(1)
    # Driver.find_element_by_xpath(DevList[i % 2]).click()
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/div/device-dir/div/div/div[2]/div/fieldset/fieldset[1]/ul/li[1]/label[2]/input').click()
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[3]/a[1]').click()
    time.sleep(1)
     #添加维护内容
    MaintenanceContest = '这是第'+ ContantList[0] + '第'+ str(i) + '个任务'
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[5]/div[2]/div/ul/li[6]/span[2]/textarea').send_keys(MaintenanceContest)
    Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[5]/div[3]/a[1]').click()

