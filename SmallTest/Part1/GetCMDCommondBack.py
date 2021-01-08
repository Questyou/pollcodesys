import os
def GoCMDCommond(order):
    Orderback = os.popen(order)
    # print(Orderback)
    f = Orderback.read()
    # print(f)
    return f

# ####################################
# ############测试命令程序#############
# testorder   =  'reg query "HKLM\Software\Microsoft\\NET Framework Setup\\NDP" /s /v version| findstr /i version | sort /+26 /r'
# GoCMDCommond(testorder)







# def add(x,y):
# #     print('和为：%d'%(x+y))