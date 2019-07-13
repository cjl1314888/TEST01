#coding=UTF8
import requests
import json
# rr=requests.get('https://www.banggood.com/ajax/event/newuserpop.html',params={'zmkm':1});
# print(rr.content);
# print(rr.url);
# print(rr.status_code);
#
# url="http://httpbin.org/get";
# r1=requests.get(url,params={"aaa":"111"});
# print(r1.url)
class aaaa():
    def gettest(self,name):
        url1 = "https://www.apiopen.top/weatherApi";
        url = "https://api.apiopen.top/searchAuthors";
        rq = requests.get(url1, params={"name": "李白", "city": name});
        print (rq.json()['data']['forecast'][0]['date']);
        print(rq.json()['data']['ganmao']);



