# . Write a program to find the maximum of the numbers in a list using the reduce 
# function. 

from functools import reduce

l = [22,55,33,56,20]

def greater(a,b):
    if(a>b):
        return a
    else:
        return b
    
print(reduce(greater,l))