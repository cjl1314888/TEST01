#coding=UTF-8
import  time
import  sys,os,glob,re,pymysql
import  requests
from  bs4 import  BeautifulSoup
from selenium import webdriver
#browser = webdriver.Firefox()
#browser.get('http://www.baidu.com/')
def testCase():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    browser = webdriver.Chrome(chrome_options=options)
    url1='http://www.baidu.com/'
    browser.get(url1)
    time.sleep(1)
    browser.find_element_by_name("wd").send_keys("詹姆斯")
    browser.find_element_by_xpath("//*[@id='su']").click()
    browser.maximize_window() # print("浏览器最大化")
    time.sleep(1);browser.set_window_size(488,888);time.sleep(1)
    browser.back();time.sleep(1)
    settest=browser.find_element_by_name("tj_briicon").text
    print(settest)
    #browser.quit()
def runCase():
    testCase()



if __name__ == '__main__':
    print("aaa")
    runCase()
