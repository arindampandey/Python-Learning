class Employee:
    company = "ITC"
    name = "Default"
    def show(self):
        print(f"The name of the employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguages(self):
        print(f"Your language is {self.language}")

class Programmer(Employee , Coder):
    company = "Infotech"
    def showlanguage(self):
        print(f"The name is {self.name} and he is good in {self.language} language")

a = Employee()
b = Programmer()

b.show()
b.printLanguages()
b.showlanguage()