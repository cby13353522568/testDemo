
"""
多行注释1
多行注释2  单引号双引号均可
"""

sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成
1"""
print(paragraph)         # 使用三引号('''或""")可以指定一个多行字符串 (python中单引号和双引号使用完全相同) ---常用于HTML或SQL
print(sentence[0:6:2])   # 字符串的截取的语法格式 : 变量[头下标:尾下标:步长]

str = 'Runoob'
# 截取，数字看字母间隔
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[2:5])  # 输出从第三个开始到第五个的字符  noo
print(str[2:])  # 输出从第三个开始后的所有字符
print(str * 2)  # 输出字符串两次
# 字符串索引
a = "Python"
print(a[1], a[-1])  # y n


# 不换行输出:变量末尾加上 end=""
print('x', end="")
print('y', end="")