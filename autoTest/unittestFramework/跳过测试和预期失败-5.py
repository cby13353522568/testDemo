import unittest


# 这些装饰器同样适用于测试类
# @unittest.skip
class MyTest(unittest.TestCase):
    @unittest.skip('直接跳过测试')
    def testA(self):
        print('a')

    @unittest.skipIf(2 < 3, '条件为真跳过测试')
    def testB(self):
        print('b')

    @unittest.skipUnless(2 < 3, '条件为真执行测试')
    def testC(self):
        print('c')

    @unittest.expectedFailure  # 不管结果如何，测试都失败
    def testD(self):
        print('d')

    @unittest.expectedFailure  # 不管结果如何，测试都失败
    def testE(self):
        self.assertEqual(3, 'e')


if __name__ == '__main__':
    unittest.main()
