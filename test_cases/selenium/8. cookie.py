from selenium import webdriver
import time, os

driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.maximize_window()

cookies = driver.get_cookies()  # 每个cookie是个字典
print(cookies)

cookie_self = {'name': 'cui', 'value': 'niubi'}
driver.add_cookie(cookie_self)

cookie = driver.get_cookie('cui')
print(cookie)

driver.delete_cookie('cui')

# driver.delete_all_cookies()

driver.quit()