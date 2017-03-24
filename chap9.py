#!/usr/bin/en python
# -*- coding: utf-8 -*-

#组织文件，适合重复复制、移动、改名数十，数百一个上文件。
import shutil  , os #shell 工具包

#9.1复制文件
# os.chdir('C:\\')
# shutil.copy('C:\\Users\\sgyy\\Desktop\\contents.txt', 'C:\\test1')
# #浏览目录
# print(os.listdir("C:\\test1"))
#拷贝当前目录下一个文件。相对路径
#shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt')

#9.2 复制文件夹
# shutil.copytree('C:\\Users\\sgyy\\Desktop\\python', 'C:\\test1\\python')
# print(os.listdir("C:\\test1"))

#9.3移动文件
# shutil.move("C:\\Users\\sgyy\\Desktop\\contents.txt", "C:\\test1\\contests.txt")
# print(os.listdir("C:\\test1"))

#9.4 unlink删除文件，rmdir空文件夹，文件夹递归删除rmtree
#9.4.1
os.chdir("C:\\Users\\sgyy\\Desktop\\trash")
path="C:\\Users\\sgyy\\Desktop\\trash"

# for filename in os.listdir():
#     if filename.endswith('.rxt'):
#         os.unlink(filename)
#容易误删文件，先print一下,安全一点
# for filename in os.listdir(path):
#     if filename.endswith('.txt'):
#         os.unlink(filename)
#         print("本次删除{}".format(filename))
# print(os.listdir(path))

#9.5 使用pip安装第三方的包 send2trash 删除文件到垃圾回收站
# C:\Users\sgyy>pip list
# beautifulsoup4 (4.4.1)
# pip (8.1.1)
# pyperclip (1.5.27)
# setuptools (20.10.1)
# virtualenv (15.0.2)
# virtualenvwrapper-win (1.2.1)
# 
# C:\Users\sgyy>pip install send2trash
# Collecting send2trash
#   Downloading Send2Trash-1.3.0.tar.gz
# Installing collected packages: send2trash
#   Running setup.py install for send2trash ... done
# Successfully installed send2trash-1.3.0
# 
# C:\Users\sgyy>pip list
# beautifulsoup4 (4.4.1)
# pip (8.1.1)
# pyperclip (1.5.27)
# Send2Trash (1.3.0)
# setuptools (20.10.1)
# virtualenv (15.0.2)
# virtualenvwrapper-win (1.2.1)
import send2trash
# send2trash.send2trash('C:\\Users\\sgyy\\Desktop\\ftp.txt')
#查看垃圾回收站，存在该文件，不能send2trash恢复垃圾回收站内容，要手动恢复

#9.6遍历目录改文件名os.walk,遍历所有目录的子目录
p="    "
for root, dirs, files in os.walk("C:\\Users\\sgyy\\Desktop\\python"):
    #print(root)
    for name in dirs:
        print(p+name+"目录")
    for name in files:
        print(p+name)
    p+=p
  
#9.7 使用zip处理压缩文件
import zipfile, os
os.chdir('C:\\Users\\sgyy\\Desktop')    # move to the folder with example.zip
exampleZip = zipfile.ZipFile('ss.zip')
print(exampleZip.namelist())
#['spam.txt', 'cats/', 'cats/catnames.txt', 'cats/zophie.jpg']
spamInfo = exampleZip.getinfo('ss.txt')
print("压缩前"+str(spamInfo.file_size))

print("压缩前"+str(spamInfo.compress_size))

print('Compressed file is %{} smaller!'.format((round(spamInfo.file_size / spamInfo.compress_size, 2))))


exampleZip.close()
#9.8 解压文件,文件会加压到指定的桌面。
import zipfile, os
# os.chdir('C:\\Users\\sgyy\\Desktop')    # move to the folder with example.zip
# exampleZip = zipfile.ZipFile('ss.zip')
# exampleZip.close()

#9.9可以解压其中某一个文件到指定位置
# import zipfile, os
# os.chdir('C:\\Users\\sgyy\\Desktop')    # move to the folder with example.zip
# exampleZip = zipfile.ZipFile('ss.zip')
# exampleZip.extract("ss.txt","C:\\")
# exampleZip.close()     

#9.10 创建压缩文件,需要制定写入的模式创建文件。第二个是指定压缩算法。zip_deflated对文件很有用
import zipfile
os.chdir('C:\\Users\\sgyy\\Desktop') 
newZip = zipfile.ZipFile('new.zip', 'w')
newZip.write('ss.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()

