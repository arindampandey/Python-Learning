# 4. Write a program to filter a list of numbers which are divisible by 5.
l = [5,1,4,2,10,53,45,90]

def divFive(n):
    if(n%5 == 0):
        return True 
    return False 

IsDivisible = filter(divFive,l)
print(list(IsDivisible))