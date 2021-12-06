# -*- coding: gbk -*-
# @Time: 2020/12/16 22:19
# @File: 5 文件读写.py
import pickle
import pprint
#文件读取 open(filename,mode) ,mode决定打开文件的方式
'''
r只读
r+读写.文件指针将会放在文件的开头
w写入 源文件会被覆盖
w+ 读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
a 追加。文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
a+ 读写.
'''

f=open("file.txt",'r+')
#all=f.read()  # 读取全部
#print(all)

line=f.readline()  #如果返回空，说明已经读到最后一行
line2=f.readline()  #如果返回空，说明已经读到最后一行
print("line1:",line)
print("line2:",line2)

line3=f.readlines()
print("line3:",line3)
for lines in line3:
    print(lines)

#f.write("\nok")

print(f.tell())   #返回当前位置，从开头开始计算

f.seek(2,0)      #光标操作
print(f.readline())
'''如果要改变文件当前的位置, 可以使用 f.seek(offset, from_what) 函数。

from_what 的值, 如果是 0 表示开头, 如果是 1 表示当前位置, 2 表示文件的结尾，例如：

seek(x,0) ： 从起始位置即文件首行首字符开始移动 x 个字符
seek(x,1) ： 表示从当前位置往后移动x个字符
seek(-x,2)：表示从文件的结尾往前移动x个字符 '''

f.close()


# pickle模块  通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储。
# 通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。
data1="pickle"
output=open("file2.txt","wb")
pickle.dump(data1,output)
output.close()
output2=open("file2.txt","rb")
data2=pickle.load(output2)
print(data2)

output.close()



