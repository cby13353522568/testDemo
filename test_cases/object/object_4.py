# -*- coding: UTF-8 -*-
# @Time: 2020/12/19 20:37
# @File: object_4.py

#冒泡
'''
a=[2,6,3,7,1]
for j in range(len(a)-1): #4
    for i in range(len(a)-1-j):
        if a[i]>a[i+1]:
            tmp=a[i]
            a[i]=a[i+1]
            a[i+1]=tmp
    print(a)

#是否质数
for num in range(1,100):
    if num == 1:
        print("1不是质数")
    else:
        for x in range(2,num):
            if  num%x==0:
                print("{}不是质数".time(num))
                print("{}={}*{}".format(num,num/x,x))
                break
        else:
            print("{}是质数".format(num))

#九九乘法
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={}".format(j,i,i*j),end=' ')
    print("")

#斐波那契数列
list=[1,1]
for i in range(2,20):
    list.append(list[i-1]+list[i-2])
print(list)

#阿姆斯特朗数
for num in range(1,10000):
    x=list(str(num))
    n=len(x)
    sum=0
    for i in range(1,n+1):
        sum+=int(x[i-1])**n
    if sum==num:
        print("{}是阿姆斯特朗数".format(num))

#最大公约数
x=int(input("输入第一个数："))
y=int(input("输入第二个数："))
if x>y:
    x,y=y,x
i=x
while i:
    if y%i==0 and x%i==0:
        print("最大公约数为：{}".format(i))
        break
    else:
        i-=1

#最小公倍数
x=int(input("输入第一个数："))
y=int(input("输入第二个数："))
if x>y:
    x,y=y,x
i=y
while i:
    if i%y==0 and i%x==0:
        print("最小公倍数为：{}".format(i))
        break
    else:
        i+=1

#30 个人在一条船上，超载，需要 15 人下船。于是人们排成一队，排队的位置即为他们的编号。
#报数，从 1 开始，数到 9 的人下船。如此循环，直到船上仅剩 15 人为止，问都有哪些编号的人下船了呢？
peple =[]
for i in range(1,31):
    peple.append(i)
c = 0
num =30
t = 0
while num >15:
    god = []
    for pe in peple:
        c += 1
        if c % 9 == 0:
            print(c,pe,'离开')
            print(peple)
            num -= 1
            god.append(pe)
    for pe in god:
            peple.remove(pe)
print('留下人员',peple)
'''

'''
A、B、C、D、E 五人在某天夜里合伙去捕鱼，到第二天凌晨时都疲惫不堪，于是各自找地方睡觉。
日上三杆，A 第一个醒来，他将鱼分为五份，把多余的一条鱼扔掉，拿走自己的一份。
B 第二个醒来，也将鱼分为五份，把多余的一条鱼扔掉拿走自己的一份。 。
C、D、E依次醒来，也按同样的方法拿鱼。
问他们至少捕了多少条鱼?
'''
fish = 1
while True:
    total, enough = fish, True
    for _ in range(5):
        if (total - 1) % 5 == 0:
            total = (total - 1) // 5 * 4
        else:
            enough = False
            break
    if enough:
        print(f'总共有{fish}条鱼')
        break
    fish += 1

