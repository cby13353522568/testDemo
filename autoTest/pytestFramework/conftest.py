import pytest

'''
本地测试配置文件
使用场景：
1、每个接口需共用到的token
2、每个接口需共用到的测试用例数据
3、每个接口需共用到的配置信息
作用范围：
只作用于所在目录及子目录
调用：   https://www.cnblogs.com/poloyy/p/12663601.html
1.conftest中fixture的scope参数为session，那么所有的测试文件执行前执行一次
2.conftest中fixture的scope参数为module，那么每一个测试文件执行前都会执行一次conftest文件中的fixture
3.conftest中fixture的scope参数为class，那么每一个测试文件中的测试类执行前都会执行一次conftest文件中的fixture
4.conftest中fixture的scope参数为function，那么所有文件的测试用例执行前都会执行一次conftest文件中的fixture
'''


# 设置测试钩子
@pytest.fixture(scope='module')
def test_login():   # 在test_first_pytest.py 的测试方法中，添加def test_answer(test_login)，则这个方法直接调用钩子函数
    print('begin')
