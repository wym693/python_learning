#!/usr/bin/en python
# -*- coding: utf-8 -*-
import re


#正则表达式例子
#不使用正则表达式判断美国电话号码
#不方便，臃肿，可能不全面
#123-456-7890  or (123)-(456)-(2349)
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
            return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

#print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
# print('Moshi moshi is a phone number:')
# print(isPhoneNumber('Moshi moshi'))  
# 
#案例2如果是字符串里面有电话号码，使用传统的方法判读，非常不方便，效率低下
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
 
# print('Done')
# #使用正则表达式，可以快速找到目标
# #电话号码做小小改动，如(415)-555-4242，需要改动比较多的代码
#案例3，使用正则表达式匹配
#使用正则表达式，电话号码表示成\d\d\d-\d\d\d-\d\d\d\d
#引入花括号简化\d{3}-\d{3}-\d{4}
#导入re 包，开始import
#把字符串的正则表达式模式，可以re.complie(pattern),生成表达式对象
#结合r'content',比直接转移更加方便，可读性更强
#等价r'\d\d\d-\d\d\d-\d\d\d\d'==\\d\\d\\d-\\d\\d\\d-\\d\\d\\d\\d
# 
# #re.search()如果找不目标，就会返回None，返回目标，一个Object对象
# #re.search().group(),search()如果返回找到的原始文本内容，使用这个
# 
pattern=re.compile(r'\d{3}-\d{3}-\d{4}')
search_result=pattern.search(message)
print(search_result.group())
#查找所有
#print(re.findall(pattern, message) 

#示例国内电话号码
#\d{3}-\d{8}|\d{4}-\{7,8}
cn_phone=re.compile(r"(\d{3})-(\d{8})")
content='''
机构名称：广东省蓝盾职业培训学院 
学院地址：广东省广州市天河区黄埔大道中336号御发商务大厦5层蓝盾学院（地铁A出口附近）
联系电话：020-38468375 ­­­­­­企业传真：020-38468400
企业QQ：800017068
'''
print(cn_phone.search(content).group())
print(cn_phone.search(content).group(0))
print(cn_phone.search(content).group(1))
print(cn_phone.search(content).group(2))

# 
#案例4，引入括号到表达式中
#匹配正则表达式中的某个分组。(\d\d\d)-(\d\d\d-\d\d\d\d)把电话号码分成两个分组
pattern=re.compile(r"(\d{3})-(\d{3}-\d{4})")
search_result=pattern.search(message)
# print(search_result.group(0))
# print(search_result.group())
# print(search_result.group(1))
# print(search_result.group(2))
#如果需要一次看所有的分组，groups()
print(search_result.groups())
# 
#案例，|符号，可以匹配多个表达式之中第一个，或者关系，多选一，只会返回第一个最先找到，如果
#需要返回所有，findall(),
heroRegex = re.compile (r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
print(re.findall(heroRegex,"Batman and Tina Fey."))
# 
# mo2=heroRegex.search('Tina Fey and Batman.')
# print(mo2.group())
# #如果需要匹配某个前缀开头的内容，可以使用|，匹配|,使用\|进行转义
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')

print(mo.group())
#?号，可以出现0,1，可选项，结合（）分组，实现默写部分可选
batRegex = re.compile(r'Bat(wo)?man')#r'Bat(wo)?man)'
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
# 
# #电话是否可选
phoneRegex = re.compile(r'(\d{3}-)?\d{3}-\d{4}')
mo1 = phoneRegex.search('My number is 555-4242')
print(mo1.group())
# 
#*号匹配出现次数，0以上
batRegex = re.compile(r'Bat(wo)*man')
 
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
# 
# 0-1==? 1-n==+  
# 0-n==*
#+号匹配次数，1次以上
batRegex = re.compile(r'Bat(wo)+man')
mo3 = batRegex.search('The Adventures of Batman')
print(mo3 == None)
# 
#使用{n,m},匹配出现次数，n<=次数<=m
#(Ha){3,5} 表示Ha整体出现3-5次  和      Ha{3,5},a出现3-5次
#((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
 
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
# 
#findall()，查找全部，并且返回list结果
message = '中国人民银行  bluedon_wen_2016@bluedon.com.cn  23344.***? XXX-XXX-XXXX Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
pattern=re.compile(r"\d{3}-\d{3}-\d{4}")
#findall写法=re.findall(pattern,string) ,也是pattern.findall(string)
all_results=pattern.findall(message)
print(all_results)
# 
# 
#[]定义你需要字符。[.*?]里面如果有特殊符号，不需要转移
#点-星，点号表示除了换行(\n)之外的任意字符，*表示0-n个,(.*)表示一段任意语言编写文字，直到换行为止
patter_test=re.compile(r".*")
content='''机构名称：广东省蓝盾职业培训学院 
学院地址：广东省广州市天河区黄埔大道中336号御发商务大厦5层蓝盾学院（地铁A出口附近）
联系电话：020-38468375 ­­­­­­企业传真：020-38468400
企业QQ：800017068 hello world
기구의 이름: 광동성 랜턴 직업 교육 학원\r\n
اسم المؤسسة   : مقاطعة قوانغدونغ   بلو كروس بلو شيلد من   معهد التدريب المهني
'''
print(patter_test.findall(content))

#示例
pattern_new=re.compile(r"[023344.?*]{7,}")
all_results=pattern_new.findall("88888888,*******,???????,..........,22223333***")
print(all_results)

print("找中文")
#把中文找出来  [\u4e00-\u9fa5]中国的范围 ，
#\u4e2d\u56fd\u4eba\u6c11\u94f6\u884c==unicode转换结果是中国人民
# pattern_new=re.compile(r"[\u4e00-\u9fa5]*")
#^脱字符表示非，相当于取反操作，找出不是中文内容
pattern_new=re.compile(r"[^\u4e00-\u9fa5]*")
all_results=pattern_new.findall(message)
print(all_results)
#^$ 使用脱字符号和美元符号限定开始和结束
beginsWithHello = re.compile(r'^Hello')
endsWithNumber = re.compile(r'\d$')
wholeStringIsNum = re.compile(r'^\d+$')
all_results=wholeStringIsNum.search('99832432432')
print(all_results.group())
#print(wholeStringIsNum.findall("2017"))
 
# 
# #.符合，可以匹配任何字符除了换行\n。(.*)表示一段任意语言编写文字，直到换行为止
# message='''
# 
# helloworld
# 
# hfdsafdsello
# '''
# 
# 
p=re.compile(r".ello")
 
all_results=p.findall("hello")
print(all_results)
# # (.*)表示一段任意语言编写文字，直到换行为止
# nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# mo = nameRegex.search('First Name: Al Last Name: Sweigart')
# 
#(.*?)非贪婪模式（找到匹配目标最短的，），和贪婪模式（尽可能找最长目标）
nongreedyRegex = re.compile(r'<.*?>')
mo = nongreedyRegex.search('<To serve man> for dinner.>')
print(mo.group())
#'<To serve man>'
# 
# 
# greedyRegex = re.compile(r'<.*>')
# mo = greedyRegex.search('<To serve man> for dinner.>')
# mo.group()
# #结果<To serve man> for dinner.>'
# 
#匹配单行字符串.*，和匹配所有行.* p=re.compile(r".*",re.DOTALL);
message1="helloworld\nhelloworld2\nhelloworld3"
p=re.compile(r".*");
result=p.search(message1)
print(result.group())
print("开启dot_all模式后")
p=re.compile(r".*",re.DOTALL);
result=p.search(message1)
print(result.group())
# 
#忽略大小写匹配
robocop = re.compile(r'robocop', re.I)
v=robocop.search('Robocop is part man, part machine, all cop.').group()
print(v)
# 
#替换功能sub(新内容，目标),返回替换结果，全部替换
namesRegex = re.compile(r'Agent \w+')
result=namesRegex.sub("Tom","Agent Alice gave the secret documents to Agent Bob. ====Agent ")
print(result)
# 
#替换敏感的姓名和电话号码\1****,\1 \3保留第几个分组
namesRegex = re.compile(r'(\d{3})(\d{4})(\d{4})')
result=namesRegex.sub(r'\1****\3',"13800138000 gave the secret documents to Agent Bob.")
print(result)
# 
# agentNamesRegex = re.compile(r'Agent (\w)\w*')
# result=agentNamesRegex.sub(r'\1****', ' 13800138000 Agent Alice told Agent Carol that Agent BEve knew Agent Bob was a double agent.')
# 
# print(result)
# 
#当表达式变得很复杂的时候，可以使用Verbose
#等价于phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-|\.)\d{4}
#(\s*(ext|x|ext.)\s*\d{2,5})?)')
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
# #Combining re.IGNORECASE, re.DOTALL, and re.VERBOSE
# #同时开启多种功能
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)
# 
# 
# 
# message="wenyemin@bluedon.com.cn 2538904474@qq.com "
# email=re.compile(r"\w+@\w+(\.[a-zA-Z]{2,3}){1,2}")
# print(email.search(message).group())
# #使用findall方法却无法显示所有的邮件地址\w+@\w+(\.[a-zA-Z]{2,3}){1,2}


