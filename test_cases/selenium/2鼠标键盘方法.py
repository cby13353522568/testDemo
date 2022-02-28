from selenium import webdriver
import time


from selenium.webdriver import ActionChains  # 鼠标操作类
from selenium.webdriver.common.keys import Keys  # 键盘操作类


def run():
    driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
    driver.get("https://www.baidu.com")
    driver.maximize_window()

    '''
    perform()  执行ActionChains类中存储的所有方法
    context_click()   右击
    double_click()   
    drag_and_drop()    拖动
    move_to_element()  鼠标悬停 
    '''
    element = driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
    ActionChains(driver).move_to_element(element).perform()

    time.sleep(10)

    elementKey = driver.find_element_by_xpath('//*[@id="kw"]')
    elementKey.send_keys(Keys.BACK_SPACE)    # 删除
    elementKey.send_keys(Keys.SPACE)    # 空格
    elementKey.send_keys(Keys.CONTROL, 'c')    # ctrl + c
    elementKey.send_keys(Keys.CONTROL, 'v')


    driver.quit()  # 关闭浏览器


if __name__ == '__main__':
    run()