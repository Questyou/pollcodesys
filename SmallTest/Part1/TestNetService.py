##
#
# 将已安装的net服务排序的命令
#
#
from time import sleep
import GetCMDCommondBack

getNetVersionCommond =\
    'reg query "HKLM\Software\Microsoft\\NET Framework Setup\\NDP" /s /v version| findstr /i version | sort /+26 /r'
netverion =  GetCMDCommondBack.GoCMDCommond(getNetVersionCommond)

firstnetver = netverion[25:38]   #找到第一行的版本号
if  float(firstnetver[0:3]) > 4.5 :
    print(".NET Framework 版本高于.NET 4.5  符合系统安装条件。")
else:
    print("NET Framework 版本" +str(firstnetver[0:3])+",  低于.NET 4.5     不符合安装条件!!!!!!!!!!!!!!!!!!!!!!!!")

sleep(10)
# print(firstnetver)
# try:
#     print(re.search('Version', netverion).span())  # 在起始位置匹配
# except ValueError:
#     print("查询的行里格式错误")
#     # print(re.search('com', 'www.runoob.com'))         # 不在起始位置匹配
