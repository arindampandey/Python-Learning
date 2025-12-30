class Employee:
    a = 1

class Coder(Employee):
    b = 2 

class Manager(Coder):
    c = 3

obj = Manager()

print(obj.a,obj.b,obj.c)