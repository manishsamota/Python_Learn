# . Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary. 

class Employee:
    salary = 234
    increment  =20

    @property
    def salaryAfterIncremen(self):
        return (self.salary + self.salary * (self.increment/100))
    @salaryAfterIncremen.setter
    def salaryAfterIncremen(self, salary):
        self.increment = ((salary/self.salary)-1)*100


e = Employee()
e.salaryAfterIncremen = 280.89

print(e.increment)