#!/usr/bin/en python
# -*- coding: utf-8 -*-

#异常的处理
#1.raise 手动抛出异常,单纯抛出，程序中断。
#2.try  except + raise
#

# age=input("请输入你要判断的年龄")
# try:
#     if int(age)<0:
#         raise Exception("年龄不能为负数")
#     elif int(age) >200:
#         raise Exception("不是人类的年龄")
#     else:
#         print ("输入正确")
# except Exception as err:
#     print ("出现错误，信息是："+str(err))
    
    
#3.系统反向追踪
#4.通过traceback模块，把异常记录到文件里面去
# import traceback
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('errorInfo.txt', 'w')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written to errorInfo.txt.')

#5.断言 (预判程序运行的结果，如果表达式为False记录消息)

# a=5
# b=11
# c=a+b
# c='16'
# assert type(c)==type(1),'c应该是一个数字才对'
# print(c)

#6 关闭断言功能 -O参数
# C:\Users\sgyy>python -O C:\chap10.py
# 16
# 
# C:\Users\sgyy>python  C:\chap10.py
# Traceback (most recent call last):
#   File "C:\chap10.py", line 38, in <module>
#     assert type(c)==type(1),'c应该是一个数字才对'
# AssertionError: c应该是一个数字才对
# 
#7.使用日志方式记录错误,很灵活，可以关闭，记录过程很全面很客观,还可以保存到外部文件。

import logging
from fileinput import filename
# logging.disable(logging.DEBUG)
# logging.disable(logging.WARN)
# logging.disable(logging.CRITICAL)
logging.basicConfig(filename="chap10_log.txt", level=10, format=' %(asctime)s - %(levelname)s- %(message)s')
logging.debug('Start of program')
a=5
logging.debug('Start of add operator,a={}'.format(a))
logging.info("a=5")
b=11
logging.debug('Start of add operator,b={}'.format(b))
logging.warning("warnming b=11")
c=a+b
logging.debug('Start of add operator,c={},type={}'.format(c,type(c)))
logging.critical("critical c is not number,so danger")
c='16'

print(c)
# 7.因此，建议不要在时候用print()

#动态调试，启动IDLE
#1.新建文件 或者打开需要调试的文件。
#2.保存文件 位*.py
#3.运行文件 Run Module F5
#4.设置调试 再运行弹出的窗口Debug--debgger，不要关闭窗口
#5.再次到文件编辑区运行文件,再次运行F5，
#6.可以设置断点
#方法二，使用eclipse的调试功能。双击代码设置断点，调试运行

