from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.126.com")
driver.maximize_window()
time.sleep(4)

driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
# driver.switch_to.frame(driver.find_elements_by_css_selector('iframe[id^="x-URS-iframe"]'))
driver.find_element_by_name('email').send_keys('111')
driver.switch_to.default_content()
