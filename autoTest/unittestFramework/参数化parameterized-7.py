import unittest
from selenium import webdriver
import time
from parameterized import parameterized  # 同时支持 unittest，pytest


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")


    def baidu_search(self, search_key):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)

    @parameterized.expand([('case1', 'selenium'), ('case2', 'unittest'), ('case3', 'parameterized')])
    # 每个元组即为一组数据，第一个参数为name，对应用例名称。
    def testSearch(self, name, search_key):
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 输出更详细的日志
