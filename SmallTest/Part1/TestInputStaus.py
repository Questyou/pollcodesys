import os

import sys

path = 'E:\\testinput.txt'
filename = 'testinput.txt'
def mkdir(path):
    isexists = os.path.exists(path)
    if not isexists:
        os.mkdir(path)
def openfile(filename):
    file2 = open()
    fileneirong = file2.read()
    print(fileneirong)
    if str(fileneirong) == 'This is write file Test!':
        print("验证写入数据正常")
    else:
        print("写入数据与预期不符")

def wfile():
    file = open(path , 'w')
    wdata = 'This is write file Test! '
    file.write(str(wdata))
    file.close()

mkdir(path)
# openfile(filename)
wfile()

