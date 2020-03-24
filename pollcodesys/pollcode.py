import  os
import tkinter

randstr = []

root = tkinter.Tk()  # tkinter模4

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
                print("\033[1; 31;40m 输入非法，请重新输入！！\033[0m")
                return '0'
        if showorder == 2:
        #验证方式2，验证是否为字母
            if str.isalpha(instr):
                if len(instr) != length:
                    print('\033[1; 31;40m 必须输入' +str(length)+' 个字母，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print("\033[1; 31;40m 输入非法，请重新输入！！\033[0m")
                return '0'
        if showorder == 3:
        #验证方式3 ，验证数字，校验长度
            if str.isdigit(instr):
                if len(instr) != length:
                    print('\033[1; 31;40m 必须输入' +str(length)+' 个数字，请重新输入！！\033[0m')
                    return '0'
                else:
                    return instr
            else:
                print("\033[1; 31;40m 输入非法，请重新输入！！\033[0m")
                return '0'
    else:
        print("\033[1; 31;40m 输入为空，请重新输入！！\033[0m")
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
    print("\033 [1 ; 31m " + pdata + "\033[0m")
    if typeis != 'no':
        tkinter.messagebox.showinfo("提示" , smsg  + str(len(randstr)) +
                                    '\n 防伪码文件存放位置' + datafile)
        root.withdrow()



print('end')