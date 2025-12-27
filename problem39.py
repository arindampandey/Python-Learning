# WAP using functions to find greatest of hree numbers .
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c
    
n = greatest(2,5,9)
print(n)
