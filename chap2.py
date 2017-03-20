#!/usr/bin/en python
# -*- coding: utf-8 -*-

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

#代码块
#缩进相同多行代码
#代码块可以嵌套代码块
#结束，缩进减少代码块结束

#关键字if elif else

#根据条件判断：
#根据名字打招呼
print('What is your name?')  # ask for their name
name = input()
if name=="Alice":
    print("hi,"+name)
else:
    print("hi,I don't known you who is")
print("The end!")







