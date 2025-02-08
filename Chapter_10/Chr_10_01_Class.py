class Employee:
    language ="Py"
    salary = 12000000

    @staticmethod
    def good():
        print(f"I belive that you are good")

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    
        print("This is dunder method which called automatically")
        print(f"Print the name {self.name} and age is {self.age}")

# Manish = Employee() # Object Instatiation

# print(f"The language of Manish is = {Manish.language} , and salary is = {Manish.salary}")

# Jitin = Employee()

# print(Jitin.language, Jitin.salary)

# Employee.language ="Java" # changing the value of language of class for all the objects
# print(Employee.language) #print the value of laguage for calss
# print (Manish.language) 
# Manish.language ="C++" #changing the value of langaue of only for object Manish
# print(Employee.language)
# print(Manish.language)

# # INSTANCE ATTRIBUTES 

# Employee.state = "Rajasthan" # adding attributes for all class
# Manish.age = 23 # adding attributes for object Manish that is age not for all calss

# print(f"The state is {Employee.state} and age is {Manish.age} and {Jitin.state}") # 

# # SELF PARAMETER  

# Employee.good()

Ravi  = Employee("Ravi", age=24, salary=12000000)


