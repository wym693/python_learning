#!/usr/bin/en python
# -*- coding: utf-8 -*-
#import random
from random import *
#IDLE
# span=true
# Traceback (most recent call last):
  # File "<pyshell#4>", line 1, in <module>
    # span=true
# NameError: name 'true' is not defined
# >>> spam=TRUE
# Traceback (most recent call last):
  # File "<pyshell#5>", line 1, in <module>
    # spam=TRUE
# NameError: name 'TRUE' is not defined
# >>> spam=True
# >>> type(spam)
# <class 'bool'>
# >>> spam=False
# >>> spam=(4>5)
# >>> spam
# False
# >>> spam=('42'==42)
# >>> spam
# False

#���̿��Ƶ�Ҫ�أ����ʽ������顢�ؼ���
#���ʽ��
#1.�Ƚ�
#2.�����Ʋ�������� and or not
#3.1��2�����
#4.����0,0.0���ַ���''�ȼ���False 
# while 1:
# while 'aaa':
# while 0.0001:
#     print("hello world")


#�����
#������ͬ���д���
#��������Ƕ�״����
#�������������ٴ�������

#�ؼ���if elif else

#���������жϣ�
#�������ִ��к�
# print('What is your name?')  # ask for their name
# name = input()
# if name=="Alice":
#     print("hi,"+name)
# else:
#     print("hi,I don't known you who is")
# print("The end!")

#ѭ���ı��ʣ���ʼ�㣬�����㣬�ظ���������������,���������ѭ��
#while�ؼ����﷨
#1.while����
#2.��������
#3.ð��
#4.��һ�������Ĵ����

#break �ؼ���
#breakֻ�����Լ�,ִ�к�������break�����whileѭ����

#ʵ��һ��ѭ�����5��hellworld
# time=1
# while time<=5 :
#     print("hello world")
# #     time=time+1
#     time+=1
# #while����
# print("The end")

#while ʾ��2��ѭ������������ÿ���������
# name=''
# # print ("�������������")
# # name=input()
# time=0
# while name!='�������':
#     time+=1
#     print ("�������������")
#     name=input()
#     if time==3:
#         break
# print("The end")

#continue ��ǰ��������ѭ������ִ��ʣ�ಿ�֣����¿�ʼִ���´�ѭ��
# while True:
#     print('Who are you?')
#     name = input()
#     if name != 'Joe':       #(1)
#         continue              #(2)
#     print('Hello, Joe. What is the password? (It is a fish.)') 
#     password = input()      #(3)
#     if password == 'swordfish':
#         break                 #(4)
# print('Access granted.')  #(5)                  

#forѭ���﷨
#for(����)
#��ʱ������
#in
#range(��ʼ,����,����),Ĭ��range(5)==range(0,5,1),��ʾѭ�����ٴ�
# >>> list(range(1,5,1))
# [1, 2, 3, 4]
# >>> list(range(0,5,1))
# [0, 1, 2, 3, 4]
# >>> list(range(0,5))
# [0, 1, 2, 3, 4]
# >>> list(range(5))
# [0, 1, 2, 3, 4]
# >>> list(range(0,-5,-1
# [0, -1, -2, -3, -4]
# >>> list(range(0,5,-1)
# []
# >>> list(range(5))
#ð��
#���������

for i in range(5):
    print("��{}��hello world".format(i+1))
    
#forѭ��ʾ��
total=0
for i in range(101):
    total+=i
print(total)

#import �﷨
#import �ؼ���
#ģ������
#��ѡ������ͬʱ������ģ�飬ͨ�����ŷָ�

#ʾ����import random �˽⵼�룬·��Lib�ļ����ļ�
# #������������ɢ����
# >>> random.random()        # Random float x, 0.0 <= x < 1.0
# 0.37444887175646646
# >>> random.uniform(1, 10)  # Random float x, 1.0 <= x < 10.0
# 1.1800146073117523
# >>> random.randint(1, 10)  # Integer from 1 to 10, endpoints included
# 7
# >>> random.randrange(0, 101, 2)  # Even integer from 0 to 100
# 26
# >>> random.choice('abcdefghij')  # Choose a random element
# 'c'
# 
# >>> items = [1, 2, 3, 4, 5, 6, 7]
# >>> random.shuffle(items)
# >>> items
# [7, 3, 2, 5, 6, 4, 1]
# 
# >>> random.sample([1, 2, 3, 4, 5],  3)  # Choose 3 elements


#from import �﷨
#from ģ���� import ��������*��
#ʹ��from�ؼ��ֺ󣬲�����Ҫдģ��ǰ׺��ֱ�ӵ���ģ��ĺ�����
#ʡ��ǰ׺����ʹ����ɶ��Ա�������from
p=list(range(20))
print(p)

print(shuffle(p))

print(p)
