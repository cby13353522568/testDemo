import unittest
from datetime import date
from HTMLTestRunner import HTMLTestRunner
# http://tungwaiyip.info/software/HTMLTestRunner.html 下载第三方库
# 修改HTMLTestRunner使支持python3

suits = unittest.defaultTestLoader.discover('./test_case', pattern='test*.py')
today = date.today()

if __name__ == '__main__':
    fp = open('./test_report/' + str(today) + 'report.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试环境：127.0.0.1')
    runner.run(suits)
    fp.close()
