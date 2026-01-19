try:
    a = int(input("Hiiii , Enter a number : "))
    print(a)

except Exception as e :
    print(e)

# If we want to run a code when try is successful then we use else
else:
    print("I am inside else")