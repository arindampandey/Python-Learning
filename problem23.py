# WAP to find out whether a student is pass or fail if it requires a total of 40% and total of 33% to pass . Assume 3 subjects and take input from the user .
marks1 = int(input("Enter the marks for subject 1: "))
marks2 = int(input("Enter the marks for subject 2: "))
marks3 = int(input("Enter the marks for subject 3: "))

total_percentage = ((marks1 + marks2 + marks3)/300)*100

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are passed !!")

else:
    print("You are fail")