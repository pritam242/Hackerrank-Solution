# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:20:33 2020

@author: Pritam
"""

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        running_tot= 0
        for i in range(1,n+1):
            if n%i==0:
                running_tot+=i

        return running_tot


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)