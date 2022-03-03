import unittest
from selenium import webdriver
from baidu_page import BaiduPage


class TestBaidu(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")

    def test_baidu(self):
        page = BaiduPage(self.driver)
        page.get('https://www.baidu.com')
        page.search_input = 'selenium'
        page.search_button.click()
        self.assertEqual(self.driver.title, 'selenium')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
