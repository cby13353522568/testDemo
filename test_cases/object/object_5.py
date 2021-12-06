# -*- coding: UTF-8 -*-
# @Time: 2020/12/23 21:11
# @File: object_5.py
import time
import datetime
'''
while True:
    input("")  # 如果是 python 2.x 版本请使用 raw_input()
    starttime = time.time()
    print('开始')
    try:
        while True:
            print('计时: ', round(time.time() - starttime, 0), '秒', end="\r")
            time.sleep(1)
    except KeyboardInterrupt:
        print('结束')
        endtime = time.time()
        print('总共的时间为:', round(endtime - starttime, 2), 'secs')
        break

#计算n个自然数的立方和
n=7
sum=0
while n>0:
    sum+=n*n*n
    n-=1
print(sum)

#计算数组元素之和
list=[1,2,3]
def sumList(list):
    n=len(list)
    sum = 0
    for i in range(0,n):
        sum+=list[i]
    return sum
print(sumList(list))

#数组翻转指定个数的元素
list=[1,2,3,5,6,7]  #(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
d=3
n=len(list)
def leftRoll(list,d,n):
    left=list[:d]
    right=list[d:n]
    right.extend(left)
    return right
print(leftRoll(list,d,n))

#列表中头尾元素对调
list=[1,2,3]
def headTofoot(list):
    list[0],list[-1]=list[-1],list[0]
    return list
print(headTofoot(list))
'''

#翻转列表
list=[1,2,3,4,5]
def fanzhuan(list):
    list[:]=list[::-1]
    print(list)
fanzhuan(list)
list.reverse()  #该方法没有返回值，对原列表做操作
print(list)

