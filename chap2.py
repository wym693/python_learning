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

#流程控制的要素，表达式、代码块、关键字
#表达式：
#1.比较
#2.二进制布尔运算符 and or not
#3.1和2的组合
#4.数字0,0.0，字符串''等价于False 
# while 1:
# while 'aaa':
# while 0.0001:
#     print("hello world")


#代码块
#缩进相同多行代码
#代码块可以嵌套代码块
#结束，缩进减少代码块结束

#关键字if elif else

#根据条件判断：
#根据名字打招呼
# print('What is your name?')  # ask for their name
# name = input()
# if name=="Alice":
#     print("hi,"+name)
# else:
#     print("hi,I don't known you who is")
# print("The end!")

#循环的本质：开始点，结束点，重复操作，变量递增,否则就是死循环
#while关键字语法
#1.while声明
#2.布尔条件
#3.冒号
#4.下一行缩进的代码块

#break 关键字
#break只有它自己,执行后跳出离break最近的while循环，

#实例一：循环输出5次hellworld
# time=1
# while time<=5 :
#     print("hello world")
# #     time=time+1
#     time+=1
# #while结束
# print("The end")

#while 示例2，循环结束条件是每次输入控制
# name=''
# # print ("请输入你的名字")
# # name=input()
# time=0
# while name!='你的名字':
#     time+=1
#     print ("请输入你的名字")
#     name=input()
#     if time==3:
#         break
# print("The end")

#continue 提前结束当次循环，不执行剩余部分，重新开始执行下次循环
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

#for循环语法
#for(声明)
#临时变量名
#in
#range(开始,结束,递增),默认range(5)==range(0,5,1),表示循环多少次
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
#冒号
#缩进代码块

for i in range(5):
    print("第{}次hello world".format(i+1))
    
#for循环示例
total=0
for i in range(101):
    total+=i
print(total)

#import 语法
#import 关键字
#模块名称
#可选，可以同时导入多个模块，通过逗号分隔

#示例，import random 了解导入，路径Lib文件夹文件
# #如何随机数，打散序列
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


#from import 语法
#from 模块名 import 函数名（*）
#使用from关键字后，不在需要写模块前缀，直接调用模块的函数名
#省略前缀方法使代码可读性变差，不建议from
p=list(range(20))
print(p)

print(shuffle(p))

print(p)
