'''

1.pip install pytest-html      HTML格式测试报告扩展
pytest -v ./ --html=./report/result.html

2.pip install pytest-rerunfailures       测试用例失败重试
pytest ./ --reruns 2    (pytest --reruns 重试次数 --reruns-delay 次数之间的间隔设置秒)
pytest ./ --reruns 2 --html=./report/result.html

3.pip install pytest-parallel      实现测试用例并行
pytest test.py --tests-per-worker 4     多线程同步

4.
@pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
@pytest.mark.skipif(condition, reason="")
@pytest.mark.flaky(reruns=5)   要将单个测试用例添加flaky装饰器 ，并在测试失败时自动重新运行，需要指定最大重新运行的次数

'''