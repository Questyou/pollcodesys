import xlrd

# 读取文件的内容
data = xlrd.open_workbook("D:\dackwhite\dai.xlsx")
filenamelist = ['江门市.txt','佛山市.txt','广州市.txt','中山市.txt','珠海市.txt','东莞市.txt','深圳市.txt','河源市.txt','惠州市.txt',
                '汕尾市.txt','汕头市.txt','揭阳市.txt','潮州市.txt','梅州市.txt','清远市.txt','韶关市.txt','云浮市.txt','湛江市.txt','茂名市.txt','阳江市.txt']
# studet = '1'
sheetName = data.sheet_names()

# print(len(sheetName))
#表格





# table = data.sheet_by_name(sheetName[2])

# print('总行数：' + str(table.nrows))
# # print('总列数：' + str(table.ncols))
# print('整行数：' + str(table.row_values(2)))
# f = open("D:\dackwhite\广州市.txt" , 'r+')
# for j in
# 取值
# ralisList = []
def getralis():
	strbegin = '['
	f.write(strbegin)
	strend = ']'
	for i in range(table.nrows-2):
		cel = table.cell( i+2 , 1 ).value
		print(str(cel))
		str1 = "{ "  + '"' + 'alias' +'"' + ':'+ '"' + str(cel) + '"' +','
		str2 =  '"' +   'freq'  + '"'  + ':'+ '"' + str(cel) + '"'+ '},' + '\n'
		allstr =  str1 + str2
		# f.write("[{ "  + '"' + 'alias:'+ '"' + str(cel) + '"' +',' )
		f.write(allstr)
	f.write(strend)

for j in range(len(sheetName)):
	p = j+3   #已经操作到中山市了
	table = data.sheet_by_name(sheetName[p])
	fileway = 'D:\dackwhite\\' + str(filenamelist[p])
	print(fileway)
	f = open(fileway, 'r+')
	getralis()
	f.close()

# print(ralisList)
# for line in open("D:\dackwhite\佛山市.txt" ,
# 				 'w', encoding="utf-8"):
# # 	print(line)
# # f = open("D:\dackwhite\江门市.txt")
# # 验证写Json成功
# f = open("D:\dackwhite\佛山市.txt" , 'r+')
# # content = f.readlines()
# # wcontent = f.write()
# strbegin = '['
# str1 = "{ "  + '"' + 'alias' +'"' + ':'+ '"' + str(cel) + '"' +','
# str2 =  '"' +   'freq'  + '"'  + ':'+ '"' + str(cel) + '"'+ '},' + '\n'
# strend = ']'
# allstr = strbegin + str1 + str2 + strend
# # f.write("[{ "  + '"' + 'alias:'+ '"' + str(cel) + '"' +',' )
# f.write(allstr)
#
#
#
# content = f.readlines()
# for line in content:
# 	print(line)

# 获取整行的值 和整列的值，返回的结果为数组
# 整行值：table.row_values(start,end)
# 整列值：table.col_values(start,end)