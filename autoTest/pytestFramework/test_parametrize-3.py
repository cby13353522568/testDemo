import pytest


# 第一个参数用来定义参数名称， 第二个参数每个元组都是一条测试数据， 第三个参数用来定义用例名称
@pytest.mark.parametrize('a, b ,expected', [(1, 1, 2), (2, 2, 3), (3, 3, 6)], ids=['case1', 'case2', 'case3'])
def test_add(test_login, a, b, expected):
    assert (a + b) == expected


if __name__ == '__main__':
    pytest.main(['-v'])

    # pytest - v - k print parametrize-3.py  -k 指定名称中包含'print'的用例
    # 整个目录运行，或cmd中目录直接pytest。注意py文件要以test开头
    # pytest -v parametrize-3.py --junit-xml=./report.xml 生成测试报告
    # pytest -v parametrize-3.py --pastebin=all  在线测试报告
