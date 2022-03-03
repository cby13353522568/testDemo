from base import BasePage


class BaiduPage(BasePage):
    """
    百度page层，可以封装页面上的元素
    """

    def search_input(self, search_key):  # 搜索框
        self.by_id('kw').send_keys(search_key)

    def search_button(self):
        self.by_id('su')

    def waitEle(self):
        ele = self.by_id('kw')
        self.wait(5, ele)
