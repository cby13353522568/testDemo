from calculatorDemo import Calculator
import unittest
# TestCase, Test Suite 测试套件（组装要运行的测试，可以调整执行顺序）,
# Test Runner 执行测试，返回测试结果, Test Fixture 提前准备和结束清理 setUp()/tearDown(),setUpClass()/tearDownClass()


class TestCalculator(unittest.TestCase):
    """
    TestCase提供断言方法：
    assertEqual(a, b)
    assertNotEqual(a, b)
    assertTrue(x)
    assertIn(a, b)
    ...
    """
    # def setUp(self):
    #     print("start")
    #
    # def tearDown(self):
    #     print("end")

    def test_add(self):
        c = Calculator(1, 2)
        result = c.add()
        self.assertEqual(result, 3)   # assert result == 3, 'pass'

    def test_sub(self):
        c = Calculator(6, 2)
        result = c.sub()
        self.assertEqual(result, 2)

    def test_mul(self):
        c = Calculator(2, 2)
        result = c.mul()
        self.assertEqual(result, 4)

    def test_div(self):
        c = Calculator(4, 2)
        result = c.div()
        self.assertEqual(result, 2)


if __name__ == '__main__':
    # unittest.main()   # unittest执行测试用例只会找以test开头的方法，默认是根据ASCII码的顺序加载测试用例，数字与字母的顺序为：0-9，A-Z，a-z。

    suit = unittest.TestSuite()  # 创建测试套件
    suit.addTest(TestCalculator('test_add'))
    suit.addTest(TestCalculator('test_sub'))
    suit.addTest(TestCalculator('test_mul'))
    suit.addTest(TestCalculator('test_div'))

    runner = unittest.TextTestRunner()
    runner.run(suit)