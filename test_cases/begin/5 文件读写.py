# -*- coding: gbk -*-
# @Time: 2020/12/16 22:19
# @File: 5 �ļ���д.py
import pickle
import pprint
#�ļ���ȡ open(filename,mode) ,mode�������ļ��ķ�ʽ
'''
rֻ��
r+��д.�ļ�ָ�뽫������ļ��Ŀ�ͷ
wд�� Դ�ļ��ᱻ����
w+ ��д��������ļ��Ѵ�������ļ������ӿ�ͷ��ʼ�༭����ԭ�����ݻᱻɾ����������ļ������ڣ��������ļ���
a ׷�ӡ��ļ�ָ�뽫������ļ��Ľ�β��Ҳ����˵���µ����ݽ��ᱻд�뵽��������֮��������ļ������ڣ��������ļ�����д�롣
a+ ��д.
'''

f=open("file.txt",'r+')
#all=f.read()  # ��ȡȫ��
#print(all)

line=f.readline()  #������ؿգ�˵���Ѿ��������һ��
line2=f.readline()  #������ؿգ�˵���Ѿ��������һ��
print("line1:",line)
print("line2:",line2)

line3=f.readlines()
print("line3:",line3)
for lines in line3:
    print(lines)

#f.write("\nok")

print(f.tell())   #���ص�ǰλ�ã��ӿ�ͷ��ʼ����

f.seek(2,0)      #������
print(f.readline())
'''���Ҫ�ı��ļ���ǰ��λ��, ����ʹ�� f.seek(offset, from_what) ������

from_what ��ֵ, ����� 0 ��ʾ��ͷ, ����� 1 ��ʾ��ǰλ��, 2 ��ʾ�ļ��Ľ�β�����磺

seek(x,0) �� ����ʼλ�ü��ļ��������ַ���ʼ�ƶ� x ���ַ�
seek(x,1) �� ��ʾ�ӵ�ǰλ�������ƶ�x���ַ�
seek(-x,2)����ʾ���ļ��Ľ�β��ǰ�ƶ�x���ַ� '''

f.close()


# pickleģ��  ͨ��pickleģ������л����������ܹ������������еĶ�����Ϣ���浽�ļ���ȥ�����ô洢��
# ͨ��pickleģ��ķ����л������������ܹ����ļ��д�����һ�γ��򱣴�Ķ���
data1="pickle"
output=open("file2.txt","wb")
pickle.dump(data1,output)
output.close()
output2=open("file2.txt","rb")
data2=pickle.load(output2)
print(data2)

output.close()



