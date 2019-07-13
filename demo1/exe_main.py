# coding=UTF8
import xlrd,xlwt
#from xlutils.copy import copy
from api_test import httpGet, httpPost,get_xlsx_locla

def read():
    wkbook = xlrd.open_workbook(r'.\123.xlsx')
    print(wkbook.sheet_names()[0])
    sheet1 = wkbook.sheet_by_name('mytest1')  # 打开对象sheet
    rows=sheet1.row_values(0)
    cols=sheet1.col_values(1,2,4)#取值第二列，从第三行取第四行结束
    print(rows,cols,sheet1.cell(1,1).ctype)
    cell1 = sheet1.cell(1, 0).value
    print (sheet1.ncols, sheet1.nrows, cell1)
def write():
    workbook = xlwt.Workbook(encoding='utf-8')
    booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)
    # 存第一行cell(1,1)和cell(1,2)
    booksheet.write(0, 0, 34)
    booksheet.write(0, 1, 38)
    # 存第二行cell(2,1)和cell(2,2)
    booksheet.write(1, 0, 36)
    booksheet.write(1, 1, 39)
    # 存一行数据
    rowdata = [43, 56]
    for i in range(len(rowdata)):
        booksheet.write(2, i, rowdata[i])
    workbook.save('test_xlwt.xls')

#write();
#read();
# get请求
obj1=get_xlsx_locla.xlxs_locla()
data1=obj1.get_data()#获取Excel数据


# ggg = httpGet.httpGet()#生成类对象
# ggg.getTest(data1) #请求get接口将Excel数据传过去
# ppp = httpPost.httpPost()
# ppp.postTest(data1) #请求pot接口将Excel数据传过去

# def compare(str1,str2):
#     if(str1 in str2):
#         print("yes")
#     else:
#         print("NO")
#
# list_1=["one","cm","three"]
#
# compare(list_1[1],"https://www.runoob.com/python/python-operators.html#ysf2")

def isyes():#excl判断预期结果和实际结果是否
    rrr = eval(data1[0][6])
    print(rrr[0])
    json_arr = {"isok": "ok", "result": {"key1": 468.00, "key12": "value1"}}
    if (json_arr[(rrr[0])][(rrr[1])] == (data1[0][7])):
        print("通过")
    else:
        print("不通过")
        print(data1[0][7])

isyes()