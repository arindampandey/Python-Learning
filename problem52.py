# Write a program to mine a file and find out whether it contains 'python'.
with open("file.txt") as f:
    content = f.read()

if("python" in content):
    print("yes , python is present")

else:
    print("No , python is not present")