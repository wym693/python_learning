#!/usr/bin/en python
# -*- coding: utf-8 -*-
def main():
    print("请输入你的名字")
    name=input()
    print("你输入的是:"+name)
    print("请输入你的年龄")
    age=input()
    age=int(age)
    print("age="+str(age))
    if name=='Alice':
        print("hi Alice")
    else:
        if age<12:
            print("you are kiddo")
        else:
            if age<=100:
                print("you are human")
            if age>100 and age<=2000:
                print("you are grannie")
            if age>2000:
                print("you are not undead,vampire")
            
                    
        #print("you are not alice,and you are not kid")        
    print("end")
    
if __name__=="__main__":
    main()