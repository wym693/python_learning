#!/usr/bin/en python
# -*- coding: utf-8 -*-
#函数
#函数的语法：
#def functionname():
#缩进代码块
#函数调用functionname()
#先定义后调用,次数不限制



# def hello():
#     print("hello")
# hello()
#没有参数，效率不高，通过引入参数，重用代码  

def hello(name):
    print("hello"+name)
hello("jack")
hello("Tom")

#增加返回值，屏蔽加工处理过程，关注函数的返回值类型

def hello3(name,age):
    print("hello"+name)
    result="未知"
    if int(age)<=15:
        result="未成年"
    elif int(age)>15 and int(age)<30:
        result="青壮年"    
    else:
        result="老年人"
    return result

p=hello3("tom",15)
print(p)
import random
def getAnswer(num):
    if num==1:
        print("you answer is num{}".format(num))
    elif num==2:
        print("you answer is num{}".format(num))
    elif num==3:
        print("you answer is num{}".format(num))
    elif num==4:
        print("you answer is num{}".format(num))
    elif num==5:
        print("you answer is num{}".format(num))
    elif num==6:
        print("you answer is num{}".format(num))
    elif num==7:
        print("you answer is num{}".format(num))
    elif num==8:
        print("you answer is num{}".format(num))
    elif num==9:
        print("you answer is num{}".format(num))
    else :
        print("you answer is num{}".format(num))

num=random.randint(1,9)
print("当前是数字"+str(num))
getAnswer(int(num))

#引入None值，数据类型，int,float,string，bool，
#表示一种抽象状态，任何类型没有值可以理解None，
#一定是None，首字母大写,函数没有返回值，也可理解为None返回值
#理解常见数据类型
# >>> p=None
# >>> type(p)
# <class 'NoneType'>
# >>> p=[]
# >>> type(p)
# <class 'list'>
# >>> p=(1,)
# >>> type(p)
# <class 'tuple'>
# >>> p=(1)
# >>> type(p)
# <class 'int'>
# >>> p=''
# >>> type(p)
# <class 'str'>
# >>> p=1
# >>> type(p)
# <class 'int'>
# >>> p=1.0
# >>> type(p)
# <class 'float'>
# >>> p=False
# >>> type(p)
# <class 'bool'>
# >>> p={'a':1}
# >>> type(p)
# <class 'dict'>

print("hello","world","welcome",sep="##",end="$")

#keyword argument关键字参数，需要用List and dict
#局部范围和全局范围 ,
#函数里面的是局部范围，函数里定义的变量是局部变量,只能被函数内访问（使用）
#函数外面的是全局范围，函数外定义的变量是全局变量,可以任意的函数内外访问（使用）
#如果需要函数内部访问或修改全局变量，需要用global修饰全局变量名。
student2="王五"
print("未执行之前name="+student2+"\n")
def hello4():
    student="张三"
#     print("name="+student)
#     print("name="+student2)
    student2="王四"
    print("hello4内部执行后name="+student2+"\n")
#print("name="+student)
hello4()
print("hello4()执行后name="+student2+"\n")

def hello5():
    global student2
    student2="王六"
    print("hello5内部执行后name="+student2+"\n")
hello5()
print("hello5()执行后name="+student2+"\n")

#异常捕获机制--提前把异常处理掉，避免异常导致系统中断
#try:
#缩进代码块
#except [内建]异常类型 :
#缩进代码块

# def spam(divedeBy):
#     try:
#         return 42/divedeBy
#     except ZeroDivisionError:
#         print("除数不能为零")
# print(spam(42))
# print(spam(0))
# print(spam(24))
#直接执行遇到ZeroDivisionError: division by zero
#第一次找到出现地方，增加try-except,程序不会中断。提高健壮性
#第二次改进，让方法简洁，异常处理放置外面

def spam(divedeBy):
    return 42/divedeBy
try:
    print(spam(42))
    print(spam(0))
    print(spam(24))
except ZeroDivisionError:
    print("除数不能为零")


