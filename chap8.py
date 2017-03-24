#!/usr/bin/en python
# -*- coding: utf-8 -*-
import os
from pathlib import Path
#1系统分隔符


# path=os.path.join("user","stuent","zhangsan")
# print(path)
# 
# #2为准备保存的文件生成绝对路径
# #文件名列表
# myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
# for filename in myFiles:
#         print(os.path.join('C:\\Users\\asweigart', filename))

#3当前的工作目录，获取当前程序运行的路径，切换当前路径，切换不存在的时候报异常FileNotFoundError:

# path=os.getcwd()
# print("当前的路径是:",path)
# #
# os.chdir("e:\\")
# path=os.getcwd()
# print("切换后的路径是:",path)
# 
# #4绝对路径和相对路径概念呢，.. .符号
# #创建文件夹,相应查看os.path下面的方法http://docs.python.org/3/library/os.path.html.
# 
# #os.makedirs('C:\\test1\\file\\python1')
# #os.mkdir("C:\\test1\\file\\python2")
# 
# path=r'C:\\test1\\file\\python2'
# #检查路径
# result=os.path.isabs(path)
# os.path.isabs('.')
# print(result)
# #查看当前的绝对路径
# path=os.path.abspath('.')
# print(path)
# #相对路径的跳转，从第二路径，如果跳转第一个路径。..\\..\\Windows
# result=os.path.relpath('C:\\Windows', 'C:\\spam\\eggs')
# print(result)
#最底层文件名basename 和目录名dir name
path = 'C:\\Windows\\System32\\calc.exe'
print("basename={},dir name={}".format(os.path.basename(path),os.path.dirname(path)))
#split获得路径和文件名的元组
print(os.path.split(path))
#根据系统的分隔符拆分路径元素
print(path.split(os.path.sep))
#对文件的大小和内容的操作,getsize()获得Byte(==8bit) 10Mbit（一个二进制位0|1）
print(os.path.getsize('C:\\Windows\\System32\\calc.exe'))
#查看目录内容,可以看到到目录和文件名,浏览文件夹
print((os.listdir('C:\\test1\\')))
#对文件路径的有效性进行判断os.path.exists(path)，是不是文件，是不是目录
print(os.path.exists('C:\\Windows'))
os.path.isdir('C:\\Windows\\System32')
os.path.isfile('C:\\Windows\\System32')
# 
#第二块，读写内容
#对文本进行操作。后缀.txt,notepad,文本里面内容，有序的字符串
#除了文本之外，其他是二进制的文件，用记事本打开其他文件乱码
#操作文本的步骤
# There are three steps to reading or writing files in Python.
# Call the open() function to return a File object.
# Call the read() or write() method on the File object.
# Close the file by calling the close() method on the File object.
 
# #打开一个文件
# #Opening Files with the open() Function
# 
# #helloFile = open('C:\\test1\\file\\hello.txt')
# 
# #打开模式，只读r，写入w，追加a create/read/write/append

# Character Meaning 
# 'r' open for reading (default) 
# 'w' open for writing, truncating the file first 
# 'x' open for exclusive creation, failing if the file already exists 
# 'a' open for writing, appending to the end of the file if it exists 
# 'b' binary mode 
# 't' text mode (default) 
# '+' open a disk file for updating (reading and writing) 
# 'U' universal newlines mode (deprecated) 


#helloFile = open('C:\\Users\\sgyy\\Desktop\\contents.txt','rt')
helloFile = open('C:\\Users\\sgyy\\Desktop\\contents.txt', 'r')
# 
# #第二步，read()读取所有的内容
#content=helloFile.read()
#print(content)

#content=helloFile.readlines()
#readlines(),每次读入文本一行，所有行作为，list返回
lines=helloFile.readlines()
for line in lines:
    print(line)
 
helloFile.close()   
# # #写入内容，只读模式打开文件不能写入。只能以w,a追加模式打开,w模式覆盖旧内容
# # helloFile.write("write from python")
# # 
# # print("写入成功")
# # 
# # helloFile.close() 
# #a追加打开文件
# 
# helloFile = open('C:\\test1\\file\\hello.txt', 'ra')
# lines=helloFile.readlines()
# for line in lines:
#     print(line)
# 
# 
# helloFile.write("write from python")
# print("写入成功")
# 
# helloFile.close() 
