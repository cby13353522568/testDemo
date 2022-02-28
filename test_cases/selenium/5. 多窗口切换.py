from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.maximize_window()


search_window = driver.current_window_handle    # 当前窗口句柄
print(search_window)

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

all_handles = driver.window_handles
print(all_handles)
time.sleep(5)

driver.switch_to.window(search_window)
time.sleep(5)
print(driver.title)

driver.quit()
