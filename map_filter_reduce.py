from functools import reduce
# Map Example 
l = [1,2,3,4,5]

square = lambda x : x*x

sqList = map(square,l)
print(list(sqList))

# Filter Example 
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even , l) # Syntax = filter(function name , list name)
print(list(onlyEven))

# Reduce Function Example 
def sum(a,b):
    return a+b

print(reduce(sum,l))
# Output = 15 (Because 1+2 = 3 , 3+3 = 6 , 6+4 = 10 , 10+5 = 15) 