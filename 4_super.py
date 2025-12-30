class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Coder(Employee):
    def __init__(self):
        print("Constructor of Coder")
    b = 2 

class Manager(Coder): 
    def __init__(self):
        super().__init__() # Helps to execute the base class constructor 
        print("Constructor of Manager")
    c = 3

obj = Manager()

print(obj.a,obj.b,obj.c)