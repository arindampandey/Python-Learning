# Write a program to make a copy of a text file.
with open("file.txt") as f:
    content = f.read()

with open("copy.txt" , "w") as f:
    f.write(content)
