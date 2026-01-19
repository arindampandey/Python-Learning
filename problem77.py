# 5. Write a program to find the maximum of the numbers in a list using the reduce function.
from functools import reduce 
l = [5,1,4,2,10,53,45,90]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater,l))