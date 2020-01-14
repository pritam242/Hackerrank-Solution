# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 13:11:53 2019

@author: Pritam
"""

import string

def minion_game(s):
    vowels='AEIOU'
    keivsc=0
    stusc=0

    for i in range(len(s)):
        if s[i] in vowels:
            keivsc+=(len(s)-i)
        else:
            stusc+=(len(s)-i)
    if keivsc>stusc:
        print ("Kevin", keivsc)
    elif keivsc<stusc:
        print ("Stuart", stusc)
    else:
        print ("Draw")    
    


if __name__ == '__main__':
    s = input()
    minion_game(s)