from .calculatorDemo import Calculator
import unittest


# 一个功能可以有多个用例，建议每个类对应一个测试功能
class TestAdd(unittest.TestCase):
    """add功能"""

    def test_add_int(self):
        c = Calculator(1, 2)
        result = c.add()
        self.assertEqual(result, 3)

    def test_add_float(self):
        c = Calculator(6.1, 2.2)
        result = c.add()
        self.assertEqual(result, 2)

class TestSub(unittest.TestCase):
    """sub功能"""
    pass


if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestAdd("test_add_int"))
    suit.addTest(TestAdd("test_add_float"))

    runner = unittest.TextTestRunner()
    runner.run(suit)
