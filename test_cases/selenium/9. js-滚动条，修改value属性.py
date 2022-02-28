from selenium import webdriver
import time, os

driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element_by_id('kw').send_keys('selenium')
driver.find_element_by_id('su').click()
time.sleep(2)

driver.execute_script('window.scrollTo(0,10000)')
driver.find_element_by_xpath('//*[@id="page"]/div/a[10]').click()

# 有时候text 显示在元素的value中
input_value = '你好2'
js = "document.getElementById('id').value='"+input_value+"';"
driver.execute_script(js)



driver.quit()