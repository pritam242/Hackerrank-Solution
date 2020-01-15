# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 13:05:09 2020

@author: Pritam
"""

s=input().strip()


try:
    print(int(s))

except ValueError:
    print("Bad String")
