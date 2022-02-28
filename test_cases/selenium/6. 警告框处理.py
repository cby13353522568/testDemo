from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element_by_id('s-usersetting-top').click()
driver.find_element_by_link_text('搜索设置').click()

driver.find_element_by_xpath('//*[@id="se-setting-7"]/a[2]').click()

alert = driver.switch_to.alert
print(alert.text)
# alert.accept()  # 确认
alert.dismiss()   # 取消
# alert.send_keys('1')  # 输入

driver.quit()