#!/usr/bin/en python
# -*- coding: utf-8 -*-

#使用if else elif 完成以下需求
#是否下雨？是 --》有没有伞？--》没有--->等一会？有伞--走

print('开始让计算机判断是否能走啦？')
print("下雨么？只能回答yes/no")
isRain=input()
if isRain=='yes':
	print("有伞么?只能回答yes/no")
	hasUmbre=input()
	if hasUmbre=='yes':
		print("可以外出了！")
	elif hasUmbre=="no":
		print("只能等一会")
		print("下雨么？只能回答yes/no")
		isRain=input()
        while isRain=='yes':
			print("只能等一会")
			print("下雨么？只能回答yes/no")
			isRain=input()
			if isRain=='no':
			break;
		print("可以外出了！")
elif isRain='no':
	print("可以外出了！")
else:
    print("输入错误，程序退出")


