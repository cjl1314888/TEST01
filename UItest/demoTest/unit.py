#coding=UTF-8
import unittest,traceback
import time
from selenium import webdriver
from selenium.common.exceptions import  WebDriverException


class asdasd(unittest.TestCase):
    def setUp(self):
        print("----start run--------")
    def test_getElementText(self):
        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        browser = webdriver.Chrome(chrome_options=options)
        url="http://www.baidu.com"
        browser.get(url)
        time.sleep(3)
        searchjs="document.getElementById('kw').value='科比';"
        searchbtn="document.getElementById('su').click()"
        try:
            browser.execute_script(searchjs)
            time.sleep(2)
            browser.execute_script(searchbtn)
            time.sleep(2)
            self.assertTrue(u"百度百科"in  browser.page_source)
        except WebDriverException as e:
            print("页面没有找到操作元素")
        except AssertionError as e:
            print("页面不存在断言")
        except Exception as e:
            print(traceback.print_exc())
        browser.quit()

        # bb = browser.find_element(by="xpath", value="//*[@id='su']")
        # txt = browser.find_element(by="xpath", value="//*[@class='mnav'][1]")
        # print(txt.text, txt.value_of_css_property("width"))
        # cl = browser.find_element_by_name("wd")
        # cl.send_keys("詹姆斯")
        # time.sleep(5)
        # cl.clear()
        # time.sleep(6)
        # browser.close()


    def tearDown(self):

        print("----------last run-------")





if __name__ == '__main__':
    unittest.main()

