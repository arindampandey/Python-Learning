# 3. Create a class 'Employee' and add salary and increment properties to it.
class Employee:
    salary = 20000
    increment = 20

    def show(self):
        print(f"The salary is {self.salary}Rs. and the increment is {self.increment}%")

    @property
    def SalaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @SalaryAfterIncrement.setter
    def SalaryAfterIncrement(self , salary):
        self.increment = ((salary/self.salary)-1)*100

    

o = Employee()
# o.show()

o.SalaryAfterIncrement = 21000
print(o.increment)