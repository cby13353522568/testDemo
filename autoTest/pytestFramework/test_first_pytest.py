import pytest


def inc(x):
    return x + 1


def test_answer(test_login):
    assert inc(3) == 5
    # 直接使用assert进行断言  assert b in a, assert x is True, assert x is not True


if __name__ == '__main__':
    pytest.main()
    # 用pytest环境执行， 或在py文件所在目录下用cmd 执行pytest first_pytest.py
