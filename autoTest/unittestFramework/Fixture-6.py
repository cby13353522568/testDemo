import unittest


def setUpModule():
    print('test module start')


def tearDownModule():
    print('test module end')


class MyTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("test class start")

    @classmethod
    def tearDownClass(cls):
        print("test class end")

    def setUp(self):
        print('test case start')

    def tearDown(self):
        print('test case end')

    def testCase(self):
        print('pass')

if __name__ == '__main__':
    unittest.main()
