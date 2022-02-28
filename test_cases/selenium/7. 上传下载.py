from selenium import webdriver
import time, os

driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
driver.get("https://www.baidu.com")
driver.implicitly_wait(10)
driver.maximize_window()

# 上传
file_path = os.path.abspath('.')
driver.find_element_by_id('file').send_keys(file_path + 'test.txt')

# 下载
options = webdriver.ChromeOptions()
# 第一个参数禁止弹出下载弹框  第二个参数修改下载路径
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': os.getcwd()}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)
driver.get("https://www.baidu.com")
driver.find_element_by_link_text('下载的链接').click()


driver.quit()