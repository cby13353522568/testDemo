import unittest

# 同时执行多个文件，指定目录及子目录。 执行顺序和main一样，按照数字字母顺序
suits = unittest.defaultTestLoader.discover(start_dir='./', pattern='test*.py')
# start_dir 待测试的模块名或测试目录。
# 如果测试目录unittestFramework 下还有子目录，里面还有py测试文件，那么要给子目录加__init__.py文件将目录标记为模块，才能读取到
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suits)