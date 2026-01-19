# 2. Write a program to input name, marks and phone number of a student and format it using the format function like below:

# "The name of the student is Harry, his marks are 72 and phone number is 99999888" 

name = input("Enter name : ")
marks = int(input("Enter marks : "))
phoneNum = int(input("Enter phone number : "))

print("The name of student is {}, his marks are {} and phone number is {}".format(name,marks,phoneNum))