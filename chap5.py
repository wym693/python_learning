#!/usr/bin/en python
# -*- coding: utf-8 -*-

#dict 字典数据类型,
#1.和列表一样，可以存多个元素，但是无序（存入和输入元素可能不一样）
#2.通过索引访问元素，但是索引可以使用多种数据类型（可以同时在一个dict出现多种类型做索引=key），不仅是整数
#同一dict，value也可以多种
#3.字典是键值对，键就是索引，值就是value，key是不能重复。value是可以重复（存在多个key指向一个value）
#d={1: 'tom', 2: 'lisi', 3: 'wangwu', 4: 'wangwu'}
#d={'1': 'tom', '2': 'lisi', 3: 'wangwu', 4: 'wangwu'}
#冒号一定写，不能用其他，元素间空格，不影响语法

#1.1对比list，两个列表，元素相同，顺序不一样，等值判断两个列表，结果为False
#两个字典，元素相同，顺序不一样，等值判断两个列表，结果为True

#1.2如何访问字典的元素，和新增字典的元素。==通过dict[key]去访问和添加
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}



# while True:
#     print('Enter a name: (blank to quit)')
#     name = input()
#     if name == '':
#         break
#     if name in birthdays:
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')
#1.3遍历字典元素,keys() values() items()
print(birthdays)

print ("birthdays的keys是{}".format(birthdays.keys()))

#使用keys()来输出元素,keys是一个列表？观察到每次输出元素顺序不同，是因为执行keys()函数重新生成key的列表。顺序变化了
for key in birthdays.keys():
    print("{}同学生日是{}".format(key,birthdays[key]))
    
print("#########")
#使用values()输出元素value,也是无序输出
for value in birthdays.values():
    print(value)
print("#########")
#如果每次只需要输出一个key-value对，使用items(),每个item是元组
for item in birthdays.items():
    #print(item)
    print("{}同学生日是{}".format(item[0],item[1]))
print("#########")
#优化后，for后放置两个变量，本质等价于一个元组的整体,k,v==(k,v)
for k,v in birthdays.items():
    print("{}同学生日是{}".format(k,v))


#1.4判断key,value是否存在指定的dict，in /not in

#1.5 dict.get(查找key,找不到key返回的值)

#1.6 dict.setdefault(key,value),快速实现，如果dict没有key,自动添加，如果已经存在该key，不做修改
#示例：
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'

count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

#传统的打印，
for k,v in count.items():
    print("{}={}次".format(k,v))
#美观打印的方法,python拿来主义
import pprint
pprint.pprint(count)





