#!/usr/bin/en python
# -*- coding: utf-8 -*-

print(4+4)

p=2**4;
q=100;
#print("p="+p)  Python强类型
print("p="+str(p)+"  end")# +表示是拼接
print("p={},q={}".format(p,q))#字符串格式化format
print("p={0},q={0}".format(p,q))

#理解% 求余
print(8/6)
print(8%6)
print(8%6)
print(8.0//6)
print(8.0/6)
print(8//6)#整除结果，不保留小数部分

#理解类型：整数、浮点型小数、字符串
num=-1.0;
num=1.0;
print("num是{}".format(type(num)))
num='a'
print("{}是{}".format(num,type(num)))
num='aa'
print("{}是{}".format(num,type(num)))
num="aa"
print("{}是{}".format(num,type(num)))
num='''aa''' ##文档注释
print("{}是{}".format(num,type(num)))

#字符串的拼接和替换
#+拼接
print("a"+"b"+"c")
#如果字符串和证书拼接，类型先转换str(3) str(3.0) str(False)
print("ad"+str(4)+str(3.0))
#重复输出5次同样的helloworld
print("helloWorld"*5)

#赋值符号= ，p=5;
p=5# 从右到左赋值，
q=9
n=10 
#等加于 p,q,n=5,9,10
print("p={}".format(p))
print("q={}".format(q))
print("n={}".format(n))
p,q,n=5,9,10

print("p={}".format(p))
print("q={}".format(q))
print("n={}".format(n))

#交换两个变量。
a=5
b=10
print("a={},b={}".format(a,b))

#===============================================================================
# q=a
# a=b
# b=q
# print("a={},b={}".format(a,b))
#===============================================================================
#python  
a,b=b,a 
print("a={},b={}".format(a,b))

#变量，1.单词，2.字符、数字、_ 3.不能以数字开头(运算加错,得不到正确的结果)
num1_1=0
#$num=5 不支持$作为变量名


