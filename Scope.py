# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:28:49 2020

@author: Pritam
"""

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        max=0

        for i in range(len(self.__elements)):
            for j in range(len(self.__elements)):
                absolute= abs(self.__elements[i] - self.__elements[j])

                if absolute>max:
                    max= absolute
        self.maximumDifference= max            

	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)