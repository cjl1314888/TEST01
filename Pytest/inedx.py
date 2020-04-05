# coding=utf-8

import  requests


def test_get1():
    key="124475443f4f65d02f03a3d80e561843"
    parameter={"city":"广州","key":key}
    url="http://apis.juhe.cn/simpleWeather/query"
    re=requests.get(url,params=parameter)
    result=re.json()
    print(result['reason'])
def test_get2():
    key = "3c81180c9d8d980895bd9e3ec9c36e5d"
    parameter = {"gid": "sz000882", "key": key}
    url = "http://web.juhe.cn:8080/finance/stock/hs"
    re = requests.get(url, params=parameter)
    result = re.json()
    print(result['reason'])
def test_post():
    url="https://www.banggood.com/load/shopcart/addProduct.html"
    parameter={"quantity": "1", "products_id": "1559976", "warehouse": "CN", "com": "shopcart", "t": "addProduct"}
    cook={'banggood_SID':'ea05819a66fd18f8d109e8a4de0dcfd0'}
    head={"x-requested-with":"XMLHttpRequest"}
    re=requests.post(url,data=parameter,headers=head,cookies=cook)
    result=re.json()
    print(result)
if __name__ == '__main__':
  # test_get1()
  # test_get2()
  test_post()
  print("")


