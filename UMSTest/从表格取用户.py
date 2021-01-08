import xlrd
data = xlrd.open_workbook("E:\test\test1.xlsx")

sheetName = data.sheet_names()

table = data.sheet_by_name(sheetName[0])

