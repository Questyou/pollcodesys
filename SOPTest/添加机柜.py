from selenium import webdriver
import time
from selenium.webdriver import ActionChains
import xlwt

DoorList = ['/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[3]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[4]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[5]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[6]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[7]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[8]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[9]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[4]/ul/li[10]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[5]/ul/li[3]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[5]/ul/li[4]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[5]/ul/li[5]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[5]/ul/li[6]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[5]/ul/li[7]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[5]/ul/li[8]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[5]/ul/li[9]/div',
            '/html/body/div[3]/div[2]/div/div[2]/div[1]/div[1]/div[5]/ul/li[10]/div',
            ]

FromList = ['/html/body/div[3]/div[2]/div/div[4]/div[2]/div/div/ul/li[4]/select/option[1]',
            '/html/body/div[3]/div[2]/div/div[4]/div[2]/div/div/ul/li[4]/select/option[2]',
            '/html/body/div[3]/div[2]/div/div[4]/div[2]/div/div/ul/li[4]/select/option[3]',
            '/html/body/div[3]/div[2]/div/div[4]/div[2]/div/div/ul/li[4]/select/option[4]']


OpenURL = 'http://172.17.13.92:24680//index.html?token=c33b9be2-b7f4-4f25-a0e0-695c1568f3f7#/rackMng'

Driver = webdriver.Chrome(r'd:\chromedriver.exe')
#直接进入了设备维护管理页面
Driver.get(OpenURL)

Driver.maximize_window()
time.sleep(1)
Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/div[2]/div[3]/div[2]').click()
time.sleep(1)
# Driver.switch_to_frame('newCell')
source = Driver.find_element_by_class_name('cabinet_cell_drag_desc')
# try:
for i in range(int(len(DoorList))):
    tarpath = str(DoorList[i])
    target = Driver.find_element_by_xpath(tarpath)
    print(source)
    print(target)
    actions = ActionChains(Driver)
    actions.drag_and_drop(source, target)
    # 执行动作
    try:
        actions.perform()
        time.sleep(2)
        #开始设置机柜信息
        Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/div/div/ul/li[1]/input').send_keys('第三排机柜'+ str(i))
        Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[2]/div/div/ul/li[3]/input').send_keys('5000')
        Driver.find_element_by_xpath(FromList[ i % 4]  ).click()
        time.sleep(1)
        Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[4]/div[3]/a[1]').click()
        time.sleep(2)
    except Exception as e:
        print(e)
    finally:
        print('跳过一个')
# except Exception as e:
#     print(e)
# finally:
#     Driver.quit()
#     print('OK')
    #选择机房
    #添加分类






