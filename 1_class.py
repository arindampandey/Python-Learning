class Employee:
    name = ""
    language = "Python"
    salary = 350000

obj1 = Employee()
obj1.name = "Rohan"
print(obj1.name , obj1.language , obj1.salary)

obj2 = Employee()
obj2.name = "Soham"
obj2.language = "JSS" # Here instance attribute will take preferance.
print(obj2.name , obj2.language , obj2.salary)

# Here name is object attributes and salary and language are class attributes as they directly belong to the class.
