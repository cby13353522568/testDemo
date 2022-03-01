import unittest
import time
from selenium import webdriver
from ddt import ddt, data, file_data, unpack


@ddt
class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    def baidu_search(self, search_key):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys(search_key)
        self.driver.find_element_by_id('su').click()
        time.sleep(2)

    # @data(['case1', 'selenium'], ['case2', 'ddt'], ['case3', 'webdriver'])
    # @unpack
    # def testSearch(self, name, search_key):
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + '_百度搜索')

    # @data(('case1', 'selenium'), ('case2', 'ddt'), ('case3', 'webdriver'))
    # @unpack
    # def testSearch2(self, name, search_key):
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + '_百度搜索')

    # @data({'search_key': 'selenium'}, {'search_key': 'ddt'}, {'search_key': 'webdriver'})
    # @unpack
    # def testSearch3(self, search_key):  # 字典的key与测试方法中的参数要保持一致
    #     self.baidu_search(search_key)
    #     self.assertEqual(self.driver.title, search_key + '_百度搜索')

    @file_data('ddt_data_file.json')
    @unpack
    def testSearch4(self, search_key):  # 字典的key与测试方法中的参数要保持一致
        self.baidu_search(search_key)
        self.assertEqual(self.driver.title, search_key + '_百度搜索')



    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)  # 输出更详细的日志
