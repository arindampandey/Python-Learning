a = (3,1,6,9,3,False,"Rohan",2.98)
print(a)

print(len(a)) # Length of tuple

no = a.count(3)
print(no)

i = a.index(False)
print(i)

b = ("hello","hiii")

# Concatenation
c = a + b
print(c)

# Repetition
Rep = b * 3
print(Rep)

# Membership
my_tuple = (1,2,3)
print(1 in my_tuple) # True
print(4 in my_tuple) # False

# Unpacking
x , y , z = my_tuple
print(x,y,z)

