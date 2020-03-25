import  os,  time , string , random , tkinter , qrcode
from pystrich.ean13 import EAN13Encoder
import tkinter.filedialog
import tkinter.messagebox
from tkinter import *
from string import *


root = tkinter.Tk()  # tkinter为python 标准化图形界面接口，创立跟窗口

number = '1234567890'
letter = 'ABCDEFEGHIJKLMNOPQRSTUVWXYZ1234567890'
allis = '1234567890ABCDEFEGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%^&*()_+'
i = 0
randstr = []
fourth = []
fifth = []
randfir = ""
randsec = ""
randthr = ""
str_one = ""
strone = ""
strtwo = ""
nextcard = ""
userput = ""
nres_letter = ""

# root = tkinter.Tk()  # tkinter模4

def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)

def openfile(filename):
    f = openfile(filename)
    fllist = f.read()
    f.close()
    return fllist

def inputbox(showstr , showorder, length):
    # shoestr是输入的提示信息
    instr = input(showstr)
    if len(instr) != 0 :
        #三种验证方式：1、 数字，不限位数、2、字母；3、数字且有位数显示
        if showorder == 1:
        #验证方式1，验证是否为数字
            if str.isdigit(instr):
                if instr == 0:
                    print('\033[1;31;40m 输入为零 ， 请重新输入！！ \033[0m')
                    return '0'
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return '0'
        if showorder == 2:
        #验证方式2，验证是否为字母
            if str.isalpha(instr):
                if len(instr) != length:
                    print('\033[1;31;40m 必须输入' +str(length)+' 个字母，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return '0'
        if showorder == 3:
        #验证方式3 ，验证数字，校验长度
            if str.isdigit(instr):
                if len(instr) != length:
                    print('\033[1;31;40m 必须输入' +str(length)+' 个数字，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print("\033[1;31;40m 输入非法，请重新输入！！\033[0m")
                return '0'
    else:
        print("\033[1;31;40m 输入为空，请重新输入！！\033[0m")
        return '0'


def wfile(sstr , sfile , typeis , smsg , datapath):
    mkdir(datapath)
    datafile = datapath + "\\" + sfile
    file = open(datafile , 'w')
    wrlist = sstr
    pdata = ""
    wdata = ""
    for i in range(len(wrlist)):
        wdata = str(wrlist[i].replace('[', '')).replace(']','')
        wdata = wdata.replace(''''', '').replace(''''', '')
        file.write(str(wdata))
        pdata = pdata + wdata
    file.close()
    print("\033[1;31m " + pdata + "\033[0m")
    if typeis != 'no':
        tkinter.messagebox.showinfo("提示" , smsg  + str(len(randstr)) +
                                    '\n 防伪码文件存放位置' + datafile)
        root.withdraw()

def mainmenu():
    print('''\033[1;35m
        ***********************************************************
                               企业编码生产系统
        ***********************************************************
             1. 生成6位数字防伪编码（213563型）
             2. 生成9位系列产品数字防伪编码（879-335439型）
             3. 生成25位混合产品序列码（）
             4. 生成含数据分析功能的防伪编码（）
             5. 智能批量生成带数据分析功能的防伪码
             6. 后溪不加生成防伪码
             7. EAN-13条形码批量生成
             8. 二维码批量输出；
             9. 企业粉丝防伪码抽奖
             0. 退出系统
        +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        说明：通过数字选择菜单
        \033[0m''')
def input_validation(insel):
    if str.isdigit((insel)):
        if insel == 0:
            print('\033[1;31;40m  输入非法，请重新输入   \033[0m')
            return 0
        else:
            return int(insel)
    else:
        print('\033[1;31;40m 输入非法，请重新输入  \033[0m')
        return 0


def scode1(schoice):
    #调用inputbox 对输入数据进行非空、输入合法性判断
    incount = inputbox('\033[1;32m    请输入要生成的防伪码数量 ： \33[0m' , 1, 0 )
    while int(incount)  == 0:  #如果输入的为字母或者数字0，要求重新输入
        incount = inputbox('\033[1;32m    请重新输入要生成的防伪码数量 ： \33[0m', 1, 0)
    randstr.clear()   # 清空保存批量防伪码信息的变量randstr
    for j in range(int(incount)):
        randfir = ''    #清空存储单条防伪的变量
        for i in range(6):    #循环产生单条防伪码
            randfir = randfir + random.choice(number)  # 产生数字随机因子
        randfir = randfir + '\n'   #分行展示
        randstr.append(randfir)     #将单条保存到数组中
    # 调用函数wfile 实现屏幕输出和文件输出
    wfile(randstr , 'scode' + str(schoice) + '.txt', '' , '已生成6位防伪码共计：' , 'codepath')

def scode2(schoice):
    ordstart = inputbox('\033[1;32m  请输入系列产品的数字起始号（3位）  \033[0m' , 3, 3)
    # 如果输入的不是3位数字，要求重新输入
    while int(ordstart) == 0:
        ordstart = inputbox('\033[1;32m  请正确输入系列产品的数字起始号（3位）  \033[0m', 3, 3)
    ordcount = inputbox('\033[1;32m 请输入产品系列数量 ： '  ,1 ,0)
    # 如果输入的不是3位数字，要求重新输入
    while int(ordcount) < 1 or int(ordcount) > 99999:
        ordcount = inputbox('\033[1;32m  请正确入产品系列数量 ： ')
    incount  = inputbox('\033[1;32m   请输入要生成的每个系列产品的防伪码数量   \33[0m' , 1 ,0)
    while int(incount) == 0:
        incount = inputbox('\033[1;32m   请输入要生成的防伪码数量   \33[0m' , 1 ,0)
    randstr.clear()
    for m in range(int(ordcount)):
        for j in range(int(incount)):
            randfir = ''
            for i in range(6):
                randfir = randfir + random.choice(number)
            randstr.append(str(int(ordstart) + m) + randfir + '\n')
    wfile(randstr , 'scode'+ str(schoice) + '.txt', '已生成生成9位系列产品防伪码共计:' , '' , 'codepath')



def scode3(choice):
    pass


def scode4(param, choice):
    pass


def scode5(param):
    pass


def scode6(param):
    pass


def scode7(param):
    pass


def scode8(choice):
    pass


def scode9(choice):
    pass



while i < 9:
    # 调用主程序
    mainmenu()
    choice = input('\033[1;32m  请输入您要操作的菜单选项 \33[0m')
    if len(choice) != 0:
        choice = input_validation(choice)
        if choice == 1:  #生成6位数字防伪编码
            scode1(str(choice))
        if choice == 2:  #生成6位数字防伪编码
            scode2(choice)
        if choice == 3:  #生成6位数字防伪编码
            scode3(choice)
        if choice == 4:  #生成6位数字防伪编码
            scode4('' , choice)
        if choice == 5:  #生成6位数字防伪编码
            scode5(choice)
        if choice == 6:  #生成6位数字防伪编码
            scode6(choice)
        if choice == 7:  #生成6位数字防伪编码
            scode7(choice)
        if choice == 8:  #生成6位数字防伪编码
            scode8(choice)
        if choice == 9:  #生成6位数字防伪编码
            scode9(choice)
        if choice == 0:
            i = 10
            print('正在退出系统！')
    else:
        print('\033[1;31;40m  输入非法，请重新输入 \033[0m')
        time.sleep(2)







print('end')