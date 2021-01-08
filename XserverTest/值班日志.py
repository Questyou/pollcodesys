# from selenium import webdriver
# from selenium.webdriver import ActionChains
# import time
# import xlwt
# import datetime
# import random
# Driver = webdriver.Chrome(r'd:\chromedriver.exe')
# loginurl = "http://172.17.13.239:12580/"
# Driver.get(loginurl)
# Driver.maximize_window()
# # 登录用户名
# MorningNameList = ["z7",'z2']
# AfternoonNameList = []
# EveningNameList = []
# timenow  = datetime.datetime.now()
# timeMorning = datetime.datetime.strptime(str(datetime.datetime.now().date())+'07:01:00', '%Y-%m-%d%H:%M:%S')
# timeAfternoon = datetime.datetime.strptime(str(datetime.datetime.now().date())+'12:01:00', '%Y-%m-%d%H:%M:%S')
# timeEve = datetime.datetime.strptime(str(datetime.datetime.now().date())+'18:01:00', '%Y-%m-%d%H:%M:%S')
# timeNight = datetime.datetime.strptime(str(datetime.datetime.now().date())+'23:50:00', '%Y-%m-%d%H:%M:%S')
# timeend = datetime.datetime.strptime(str(datetime.datetime.now().date())+'23:59:50', '%Y-%m-%d%H:%M:%S')
#
#
# #登录
# def login(name):
#
#     time.sleep(1)
#     login = Driver.find_elements_by_class_name("text.login_content_input")
#     # loginname = input("请输入登录用户名： ")
#     # print(loginname)
#     # login[0].send_keys(str(loginname))
#
#     # login[0].send_keys(name)
#     # login[1].send_keys('123456')
#     login[0].send_keys('admin')
#     login[1].send_keys('Bohui@123')
#     Driver.find_element_by_class_name('button.bt').click()
#     time.sleep(1)
#     # usernameList  =  ['zhangx']
#     # realnameList  =  ['zhangxin']
#
# # 访问值班日志
# def findzhiban():
#     time.sleep(1)
#     # Driver.find_element_by_tag_name("a[title=值班综合管理系统]")
#     # Driver.find_element_by_xpath("//*[title=值班综合管理系统]")
#     # Driver.find_element_by_link_text("值班综合管理系统").click()
#     #权限分配好的话，值班人员登录后直接会进入值班日志填写页面
#     Driver.find_element_by_css_selector("div[title='值班综合管理系统'][class='system_list_li_txt']").click()
#     #这部分先不管了，通过权限控制用户直接登录到
#     # time.sleep(10)
#     # Driver.find_element_by_xpath("//span[text()=\"值班管理\"]").click()
#     # time.sleep(1)
#     # Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[4]/nav/ul/li[2]/ul/li[1]/div[2]').click()
#     # 进入值班日志页面
#     time.sleep(2)
# # 获取交班人员信息
#
# # 交接班
# def change(num,name):
#     time.sleep(2)
#     # 点击接班按钮，位置需要随着变化
#     changebutton = '/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[12]/td['+ num + ']/p/button'
#     Driver.find_element_by_xpath(changebutton).click()
#     time.sleep(3)
#     Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/input[1]').send_keys(name)
#     Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/input[2]').send_keys('123456')
#     time.sleep(20)
#     Driver.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div/button').click()
#     # 等待接班完成
#     time.sleep(5)
#
# def Logout():
#     time.sleep(3)
#     # 点击用户名
#     Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[1]/span').click()
#     time.sleep(1)
#     # 点击注销
#     Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div/div[3]/div[1]/div[2]/div/div[2]/div[2]/div/div/div[2]').click()
#     time.sleep(1)
#     # 确认注销
#     Driver.find_element_by_xpath('/html/body/div[5]/div[2]/button[1]').click()
#     time.sleep(1)
# #  设置接班基本信息
# def inputordermsg(pathnum):
#     time.sleep(3)
#     #温湿度
#     temp = random.randint(10 , 60)
#     shidu = random.randint(20 , 100)
#     print(temp,shidu)
#     # 温湿度的位置
#     tempPathList = ['/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[2]/td[2]/input',
#                     '/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[2]/td[3]/input',
#                     '/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[2]/td[4]/input',
#                     '/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[2]/td[5]/input']
#
#
#
#     Driver.find_element_by_xpath(tempPathList[]).send_keys(temp)
#     Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[3]/td[3]/input').send_keys(shidu)
#     # 五个常规操作
#     for i in range(5):
#         buttonpath = '/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[4]/td[' + str( pathnum +1 ) + ']/p[ ' + i +']/input'
#         Driver.find_element_by_xpath(buttonpath).click()
#     # Driver.find_element_by_xpath(').click()
#     # Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[4]/td[3]/p[2]/input').click()
#     # Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[4]/td[3]/p[3]/input').click()
#     # Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[4]/td[3]/p[4]/input').click()
#     # Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[4]/td[3]/p[5]/input').click()
#     # # PGM 信息
#     PGMmsg = "PGM Msg"
#     # PGMtxt = '/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[4]/td[' + str(pathnum) +
#     Driver.find_element_by_xpath(
#         '/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[6]/td[3]/input').send_keys(PGMmsg)
#     # 保存配置信息
#     Driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[3]/div/div/div/div[1]/div[2]/button').click()
#     time.sleep(1)
#     # #信号源信息
#     # singnalmsg = "信源正常"
#     # Driver.find_element_by_xpath(
#     #     '/html/body/div[1]/div[1]/div[3]/div/div/div/div[2]/table[1]/tr[5]/td[3]/textarea').send_keys(singnalmsg)
#
# def MorningChange():
#     for i in range((len(MorningNameList))):
#         name = MorningNameList[i]
#         login(name)
#         # 交接班按钮位置
#         changebtn = i+1
#         change( changebtn , name)
#         inputordermsg(changebtn)
#         Logout()
#         i += 1
#         print("第" + str(i) + '次交接班')
#     print("end")
#
#
# # # 等待时间到达
# # # 时间节点
# # morningsignal = False
# # afternoonsignal = False
# # eveningsignal = False
# # nightsignal = False
# # #判断是不是到了改交接班的时间了：
# # sign = True
# # while sign:
# #     print(afternoonsignal)
# #     if timenow > timeMorning  and morningsignal == False:
# #         print("do MorningChange")
# #         morningsignal == True
# #     if timenow > timeAfternoon  and afternoonsignal == False:
# #         print("do AfternoonChange")
# #         afternoonsignal = True
# #     if timenow > timeEve and eveningsignal == False:
# #         print("do AfternoonChange")
# #         eveningsignal = True
# #     if timenow > timeNight and nightsignal == False:
# #         print("do AfternoonChange")
# #         nightsignal = True
# #     if timenow > timeend:
# #         morningsignal = False
# #         afternoonsignal = False
# #         eveningsignal = False
# #         nightsignal = False
# #         time.sleep(1200)
# #     else:
# #         timenow = datetime.datetime.now()
# #         time.sleep(20)
# #         print(timenow)
# #         print('do nothing')
#
# Driver.close()
