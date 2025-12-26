# WAP to find sum of n natural numbers using while loop .
n = int(input("Enter the value of n : "))

i = 0
sum = 0
while(i<=n):
    sum = sum + i
    i += 1

print(f"Sum = {sum}")
