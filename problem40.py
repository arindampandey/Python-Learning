# WAP using function to convert from celcius to fahrenheit .
def F_to_C(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = F_to_C(f)
print(f"{round(c , 2)} °C")
