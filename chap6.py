#!/usr/bin/en python
# -*- coding: utf-8 -*-

#String字符串的处理方法，（转换大小写，去除空格，特殊符号，获取剪贴板字符串）

#1.1常见字符串表示方法： '字符串',"字符串",'''字符串''',r"字符串原来的样子"

#1.2常见的转义符 
#\' 原样出现'
#\n 末尾换行 
#\\ 原样出现\
#\t 缩进
#\" 原样出现"

#1.3 raw string和'''符号区别，r修饰字符串，原封不动，原样输出，而'''修饰字符串，换行，缩进保留，但是转义符生效的

# str =r"fdsfdsfds\n \\ \'"
# print (str)
# 
# print("########")
# str2='''fdsafdsafds    fdsafdsa         
# fdsafdsafdsa\n
# fdsa\\
#     fdsfds\f
#     中文
# 
# 
# 
# '''
# str3=r'''fdsafdsafds    fdsafdsa         
# fdsafdsafdsa\n
# fdsa\\
#     fdsfds\f
#     中文
# 
# 
# #1.4 单行注释#和多行注释""",多行注释不能放在代码本行后
# '''
# #这里是注释
# """
# 这里是注释这里是注释这里是注释这里是注释这里是注释
# 这里是注释这里是注释这里是注释这里是注释这里是注释
# 这里是注释这里是注释这里是注释这里是注释这里是注释
# 这里是注释这里是注释这里是注释这里是注释这里是注释
# 
# 这里是注释这里是注释这里是注释这里是注释这里是注释
# """
# print (str2) #这里是注释
# print("########")
# print (str3)

#1.5 字符串使用list的索引访问和切片操作，也使用in和not in操作

#1.6 字符串的常用方法，upper()，lower() isupper(),islower()


#1.7 判断字符串是否是字母，字符和数字，数字，空格，标题
#isalphe(),isalnum(),isdicimal(),isspace(),istitle()

#1.8 判断字符串的开头和结尾是否满足要求，startswith(),endswith()

# #1.9
# sentence="welcome to bluedon"
# t=list[sentence]
# t=['w', 'e', 'l', 'c', 'o', 'm', 'e', ' ', 't', 'o', ' ', 'b', 'l', 'u', 'e', 'd', 'o', 'm']
# str=''
# for ch in t:
#     str+=ch
# print (str)

#1.9需要使用,空格分隔每个单词,可以使用join，用某个符号去连接列表中的每一个元素
# ", ".join(["welcome","to","bluedon"])

#需要把字符串拆分列表,split()
# sentence="welcome to bluedon"
# result=sentence.split()
# print(result)
# result2=" ".join(result)
# print(result2)

#2.0 ljust() rjust() center 把目标放在哪里（左右中），剩下填充空格。
#实现购物小票的对齐打印

# sentence="hello"
# print(sentence.rjust(10))
# 
# print(sentence.ljust(10))
# 
# print(sentence.center(10))
# 
# #2.1 使用pyperclip 操作系统的剪贴板
# import pyperclip
# #复制内容到剪贴板
# pyperclip.copy("bluedon")
# 
# #粘贴功能
# pyperclip.paste()

#chap6_练习二，自动化添加每一行的*


# 处理完后
# 
# * Lists of animals
# * Lists of aquarium life
# * Lists of biologists by author abbreviation
# * Lists of cultivars

import pyperclip
#读取需要处理的内容到text
text = pyperclip.paste()


print("处理前内容是{}".format(text))

# TODO: Separate lines and add stars.

lines = text.split('\n')
for i in range(len(lines)):    # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" lis
print("处理完后lines={}".format(lines))

text="\n".join(lines)



pyperclip.copy(text)

print("end")


