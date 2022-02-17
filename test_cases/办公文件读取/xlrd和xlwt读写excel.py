from xlwt import *
from xlrd import *


def write():
    file = Workbook(encoding='UTF-8')
    sheetName = file.add_sheet("sheet1")
    sheetName.write(0, 0, "111")
    file.save("xlwt写入excel.xlsx")


def read(file_path):
    file = open_workbook(file_path)
    sheet1 = file.sheets()[0]
    print('表格总行数', sheet1.nrows)
    print('表格总列数', sheet1.ncols)
    cellValue = sheet1.cell(0, 0).value
    print(cellValue)


if __name__ == '__main__':
    # write()
    read("xlwt写入excel.xlsx")

