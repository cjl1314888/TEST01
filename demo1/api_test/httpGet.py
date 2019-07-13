# coding=UTF8
import requests


class httpGet:
    def getTest(self, list_data):
        for x in range(len(list_data)):
            if list_data[x][1]=="get":
                if((list_data[x][3])!=""):dic1=eval(list_data[x][3])
                else:dic1=""
                if((list_data[x][4])!=""):cook=eval(list_data[x][4])
                else:cook=""
                if((list_data[x][5])!=""):header=eval(list_data[x][5])
                else:header=""
                url =list_data[x][2]
                #print (type(dic1))
        re = requests.get(url, params=dic1, headers=header, cookies=cook)
       # print (re.json()['data']['forecast'][0]['date']);
       # print(re.json()['data']['ganmao']);
        print(re.json())
        return 1;
