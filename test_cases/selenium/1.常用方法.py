from selenium import webdriver
import time, os

def run():
    driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
    # driver = webdriver.Chrome()   # 得把ChromeDriver添加到环境变量
    driver.get("https://www.baidu.com")

    driver.maximize_window()   # driver.set_window_size(400,400)

    # 后退，前进
    # driver.back()
    # driver.forward()

    # 刷新
    # driver.refresh()

    # 常用方法
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('你好')  # 输入
    # driver.find_element_by_xpath('//*[@id="su"]').click()     # 点击
    # driver.find_element_by_xpath('//*[@id="kw"]').clear()     # 清空

    print(driver.find_element_by_xpath('//*[@id="kw"]').text)   # 获取元素文本

    print(driver.find_element_by_xpath('//*[@id="kw"]').get_attribute('value'))   # 获取元素属性值
    print(driver.find_element_by_xpath('//*[@id="kw"]').size)   # 获取元素尺寸
    print(driver.find_element_by_xpath('//*[@id="kw"]').is_displayed())   # 获取元素是否可见

    driver.find_element_by_xpath('//*[@id="kw"]').submit()  # 相当于回车

    driver.save_screenshot(os.getcwd())   # 截图





    driver.close()  # 关闭当前页
    # driver.quit()  # 关闭浏览器


if __name__ == '__main__':
    run()