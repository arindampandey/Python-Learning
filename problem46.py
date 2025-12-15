# WAP to print multiplication table of a given number using function.
def table(n):
    for i in range(1,11):
        print(f"{n} X {i} = {n*i}")

    
a = int(input("Enter a number : "))
print(table(a))