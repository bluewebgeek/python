# -*- coding: utf-8 -*-
import os

# Creates a list containing 5 lists initialized to 0

Matrix = [[0 for x in range(5)] for x in range(5)] 
Matrix [0][0]=1
print Matrix[0][0]


def MyClass(number):
    def __init__(number):
        self.number=number
     

my_objects = []         
for i in range(5):
   print i            
   my_objects.append(MyClass(i))

print my_objects