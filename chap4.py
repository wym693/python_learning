#!/usr/bin/en python
# -*- coding: utf-8 -*-

#list 列表=存储按照顺序排列的多个值类型（值可以是不同类型），可以存储重复值
# >>> p=[]
# >>> type(p)
# <class 'list'>
# >>> p=[1,2,3,4]
# >>> type(p)
# <class 'list'>
# >>> p
# [1, 2, 3, 4]
# >>> p=[1,2,3,4,4,4,4,4,4,4,4]
# >>> p
# [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4]
# >>> p=[1,2,3,4,4,4,4,4,4,4,4,'4',4.0]
# >>> p
# [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, '4', 4.0]
# >>>
# 1.1访问列表的某一个元素，使用索引[正负整数，负数下标表示倒数第几个，-1==倒数第一个]
#   -len(p)<=index<len(p)

#1.2 列表切片(获取列表局部) p[startindex:endindex+1],包括开始下标元素，
#不包括结束下标元素，特殊，结束位置包含末尾元素，可以不写下标

#1.3 修改列表元素值，通过下标访问
# [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, '4', 4.0]
# >>> p[-1]=5.0
# >>> p
# [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, '4', 5.0]
# >>> p[12]=6.0
# >>> p
# [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, '4', 6.0]
# >>> p[-1]=p[-3]
# >>> p
# [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, '4', 4]
# >>>
#1.4.列表的拼接和替换，参考string 拼接和多次重复用乘法
# >>> q=['a','b','c']
# >>> p+q
# [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, '4', 4, 'a', 'b', 'c']
# >>> q*3
# ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
#1.5 列表元素的删除操作 ，del 关键字
# >>> q
# ['a', 'b', 'c']
# >>> del q[1]
# >>> q
# ['a', 'c']

#1.6 使用列表工作，循环录入，循环输出 for 

students=[]
#循环录入
# for i in range(6):
#     print("请输入第{}个同学的名字".format(i+1))
#     name=input()
#     if name is None or name =="":
#         print ("name是空值，请输入内容")
#         continue
# #     students.append(name)
#     students=students+[name]
# #循环输出
# for i in range(len(students)):
# #     print (name+"\n")
#     print("请输入第{}个同学的名字是{}".format(i+1,students[i]))

#1.7 使用列表赋值
# >>> n=[1,2,3]
# >>> c,b,a=n
# >>> b
# 2
# >>> a
# 3
# >>> c
# 1
# >>>
#1.8 +=符号，自加操作 total+=1 等价于 total=total+1
#


#1.9 列表的增删查改第二套方法，函数 remove(item),index(item),append(item),insert(index,item)
# p=[5,1,2,3,4,5,5,5,5,5,5,5,5,5,5]
# 
# while 5 in p:
#     p.remove(5)
# print(p)


#2.0 列表排序
# >>> p
# [6, 1, 2, 3, 4, 5]
# >>> p.sort()
# >>> p
# [1, 2, 3, 4, 5, 6]
# >>> p.sort(reverse=True)
# >>> p
# [6, 5, 4, 3, 2, 1]
#2.1 python 代码缩进例外，list元素中缩进没有任何意义，不影响程序

#2.2 长得像list 有tuples string,list功能和函数，string,tuples也有
#字母列表组装成句子
# t=['w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'b', 'l', 'u', 'e', 'd', 'o', 'm']
# str=''
# for ch in t:
#     str+=ch
# print (str)

#2.3 可变和不可变的值类型。
#string创建之后，字符串元素item不能修改值，p="tom",p[1]='a'操作不允许


#2.4 list tuple string相互转换,使用对应
#list(tuple/string),tuple(list/string) str(list/tuple)
p=[1,2,3,4]
p=tuple(p)
print (type(p))

p=str(p)

print (type(p))

#引用传递和值传递 ，引用传递相当于快捷方式，只有一个目标文件
#而值传递的，相当于原件的副本。最终两个目标文件

a=5
b=10

def swap(num1,num2):
    print("num1={},num2={}".format(num1,num2))
    num1,num2=num2,num1
    print("num1={},num2={}".format(num1,num2))
    
print("交换前：a={},b={}".format(a,b))
swap(a,b)
print("交换后：a={},b={}".format(a,b))

def swap2( num1, num2):
    
    num1,num2=num2,num1
    



c=[1,2,3]
d=c
 
# print("交换前：c={}".format(c))
# change(c)
# print("交换前：c={}".format(c))

def change(obj):
#    obj.append("egg")
    obj+=1

print("a={}".format(str(a)))
change(a)
print("a={}".format(str(a)))


#copy模块 把原来是引用传递的list，也可以当成值传递
import copy

p=[1,2,3,4,5]
q=p;
print("p.id={},q.id={}".format(id(p),id(q))) 
#相同id，表示指向同一个目标
q[1]=100
print("p={},q={}".format(p,q)) 
#赋值list内容
t=copy.copy(p)
t[2]=100
print("p={},t={}".format(p,t)) 

#实验，写函数把列表传入，输入字符串

def  changeList(l):
    str_temp=''
    #for item in l:
#         str_temp+=item+", "
    for i in range(len(l)):
        if i==(len(l)-1):
            str_temp+=l[i]
        else:
            str_temp+=l[i]+", "
    return str_temp

content=['welcome','to','bluedon']
print(changeList(content))


grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
#原来样子
for y in grid:
    temp=""
    for x in y:
        temp+=x
    print(temp)
#顺时针转90°

for x in range(len(grid[0])):
    temp=""
    for y in range(len(grid)):
        temp+=grid[y][x]
    print(temp)






