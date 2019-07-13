# coding=utf-8
import  xlrd
class xlxs_locla:
    def get_data(self):
        wds=xlrd.open_workbook(r'.\api_test\api_getAndPost.xlsx')
        sheet1=wds.sheet_by_name("api_test_case")
        rows=sheet1.row_values(0)
        #print(rows)
        list=[]
        for x in range(sheet1.nrows-1):
            #print(sheet1.row_values(x+1))
            list.append(sheet1.row_values(x+1))
        return list