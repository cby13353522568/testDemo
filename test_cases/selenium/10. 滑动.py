from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import time


driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.helloweba.net/demo/2017/unlock")
driver.implicitly_wait(10)
driver.maximize_window()

slider = driver.find_elements_by_class_name('slide-to-unlock-handle')[0]
size = driver.find_elements_by_class_name('slide-to-unlock-bg')[0].size['width']
action = ActionChains(driver)
action.click_and_hold(slider)  # 单击并按下
while True:
    try:
        action.move_by_offset(size, 0).perform()   # 移动鼠标
        # action.reset_actions()
    except UnexpectedAlertPresentException:
        break


time.sleep(5)


driver.quit()