# Create a Class "Programmer" for storing information of few programmers working at Microsoft.
class Programmer:
    company = "Microsoft"
    def __init__(self , name , salary , pin):
        self.name = name
        self.salary = salary
        self.pin = pin

obj1 = Programmer("Rohan",120000,1234)
print(obj1.name,obj1.salary,obj1.company)

obj2 = Programmer("Soham",150000,1235)
print(obj2.name,obj2.salary,obj2.company)



