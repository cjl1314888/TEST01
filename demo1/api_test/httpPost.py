# coding=UTF8
import requests
class httpPost:

    def postTest(self,list_data):
        #print(list_data[0])
        for x in range(len(list_data)):
            if list_data[x][1]=="post":
                if ((list_data[x][3]) != ""):dic1 = eval(list_data[x][3])
                else: dic1 = ""
                if ((list_data[x][4]) != ""):cook = eval(list_data[x][4])
                else:cook = ""
                if ((list_data[x][5]) != ""):header = eval(list_data[x][5])
                else:header = ""
                url =list_data[x][2]
                #print (type(dic1))
                re = requests.post(url, data=dic1, headers=header, cookies=cook)
                result = re.text
                print(result);
        return 0;
