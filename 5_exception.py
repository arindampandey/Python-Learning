try:
    a = int(input("Hiiii , Enter a number : "))
    print(a)

except ValueError as v :
    print("Hi")
    print(v)

except Exception as e :
    print(e)

print("Thank You !!")