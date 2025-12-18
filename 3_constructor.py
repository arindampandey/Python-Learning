class Employee:
    name = ""
    language = "Python"
    salary = 350000

    def __init__(self , name , salary , language):
         self.name = name 
         self.salary = salary
         self.language = language 
         print("Creating an object")

    def getinfo(self):
            print(f"The language is {self.language} and the salary is {self.salary}")
 
    def greet(self):
        print("Hello , how are you ?? ")  

obj = Employee("rohan" , 120000 , "JSS")

obj.getinfo()
obj.greet()