# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 12:16:27 2020

@author: Pritam
"""

rom abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class

class MyBook(Book):
    def __init__(self,title,author,price):
        super().__init__(title,author)
        self.price=price

    def display(self):
        print("Title: "+self.title+"\nAuthor: " + self.author + "\nPrice: " + str(self.price))    

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()