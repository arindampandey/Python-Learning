a = int(input("Enter first number : "))
b = int(input("Enter second number : "))

if(b == 0):
    raise ZeroDivisionError("This condition is not possible in this programm")
else:
    print(f"The division is {a/b}")