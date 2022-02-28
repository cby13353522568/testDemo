from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def run():
    driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chromedriver.exe")
    driver.get("https://www.baidu.com")
    driver.maximize_window()

    # 显示等待  -- 等到某个条件成立才继续执行  WebDriverWait(driver, 超时时间, 检测间隔),长和until(method)或until_not()一起使用
    # element = WebDriverWait(driver, 5, 1).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="kw"]')))
    element = WebDriverWait(driver, 5, 1).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="kw"]')), '超时！')
    '''
    EC.presence_of_all_elements_located   元素是否存在 ，如果不存在则TimeoutException 
    EC.title_is
    EC.visibility_of 元素是否可见
    EC.text_to_be_present_in_element    元素中的text是否包含预期字符串
    EC.element_to_be_clickable   元素是否可以点击
    EC.element_to_be_selected    元素是否被选中
    '''

    # 第二种方式实现：
    for i in range(5):
        try:
            el = driver.find_element_by_xpath('//*[@id="kw2"]')
            if el.is_displayed():
                break
            else:
                time.sleep(1)
        except:
            pass
    else:
        print('timeout')

    # 隐式等待 -- 需要等待页面全部元素加载完成，才会执行下一个语句
    driver.implicitly_wait(10)  # 隐式等待10秒
    # 隐式等待相比强制等待更智能，在脚本中我们一般看不到等待语句，但是它会在每个页面加载的时候自动等待；隐式等待只需要声明一次，一般在打开浏览器后进行声明。声明之后对整个drvier的生命周期都有效

    driver.quit()  # 关闭浏览器


if __name__ == '__main__':
    run()
