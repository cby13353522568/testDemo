# -*- coding: UTF-8 -*-
# @Time: 2020/12/8 21:38
# @File: base_2_1.py

def reverseWord(input):
    """ 反转字符串 """
    inputWord = input.split(" ")  # 通过空格将字符串分隔符，把各个单词分隔为列表
    print(inputWord)
    outputWord = inputWord[-1::-1]  # 第一个参数 -1 表示最后一个元素,第二个参数为空，表示移动到列表末尾,第三个参数为步长，-1 表示逆向
    output = " ".join(outputWord)
    return output


if __name__ == "__main__":
    input = "I like python"
    print(reverseWord(input))
    print(reverseWord.__doc__)  # 输出函数的注释
