class Employee: # Base Class 
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} nd the salary is {self.salary} ")

class Programmer(Employee): # Derived Class
    company = "Infotech ITC"
    def showLanguage(self):
        print(f"The employee {self.name} is good in language {self.language}")

a = Employee()
b = Programmer()

print(a.company , b.company)