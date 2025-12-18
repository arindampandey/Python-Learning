class Employee:
    name = ""
    language = "Python"
    salary = 350000

    def getinfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    # def greet():
    #     print("Hello , how are you ?? ") # It will throw an error
    
    @staticmethod
    def greet(self):
        print("Hello , how are you ?? ")  

    def greet(self):
        print("Hello , how are you ?? ")  

obj = Employee()

obj.getinfo()
obj.greet()