# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:14:25 2020

@author: Pritam
"""

num = int(input())

result = 0
maximum = 0

while num > 0:
    if num % 2 == 1:
        result += 1
        if result > maximum:
            maximum = result

    else:
        result = 0

    num //= 2

print(maximum)
