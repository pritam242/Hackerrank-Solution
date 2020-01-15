# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 10:53:24 2020

@author: Pritam
"""

n=int(input())

phone_book={}

for i in range(0,n):
    entry= input().split(" ")
    
    
    name=entry[0]
    phone_num=int(entry[1])
    
    phone_book[name]= phone_num
    
    """query for presence of name in the phone book"""
    
for j in range(0,n):
    name=input()
    
    if name in phone_book:
        phone_num=phone_book[name]
        print(name + "=" + str(phone_num))
    else:
        print("Not found")
    