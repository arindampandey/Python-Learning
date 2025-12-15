# Write a function which converts inches to centimeters.
def inc_to_cm(i):
    cm = i * 2.54
    return cm

i = int(input("Enter the value in inches : "))
print(f"The value in cm is : {inc_to_cm(i)}")