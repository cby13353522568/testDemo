import time


class BasePage:
    """
    基础 Page层，封装常用方法
    """
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    # id 定位
    def by_id(self, id_):
        return self.driver.find_element_by_id(id_)

    # 元素等待
    def wait(self, second, element):
        for i in range(second):
            try:
                if element.is_displayed():
                    break
                else:
                    time.sleep(1)
            except:
                pass
        else:
            print('timeout')
