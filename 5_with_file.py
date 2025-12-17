f = open("file.txt")
print(f.read())
f.close()

# The same can be written as : 
with open("file.txt") as f:
    print(f.read())

# Using this method you dont have to close the file explicitly