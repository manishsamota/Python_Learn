# SINGLE INHERITANCE -> Single inheritance occurs when child class inherits only a single parent class. 

# base class -> child class

# class Company:
#     company ="Microsoft"
#     country="USA"

# class Employee(Company):
#     name ="Manish"
#     salary="120000000"

# b = Employee()

# print(b.company)
# print(b.name)

# MULTIPLE INHERITANCE 

# Multiple Inheritance occurs when the child class inherits from more than one parent classes.

# class Company:
#     company ="Microsoft"
#     country="USA"

# class Uni:
#     uni_name = "Lincoln"

# class Employee(Company, Uni):
#     name ="Manish"
#     salary="120000000"

# b = Employee()

# print(b.company)
# print(b.name)
# print(b.uni_name)


#  MULTILEVEL INHERITANCE 
# When a child class becomes a parent for another child class. 

# class Company:
#     company ="Microsoft"
#     country="USA"

# class Uni(Company):
#     uni_name = "Lincoln"

# class Employee(Uni):
#     name ="Manish"
#     salary="120000000"

# b = Employee()

# print(b.company)
# print(b.name)
# print(b.uni_name)


# SUPER() METHOD 
# super() method is used to access the methods of a super class in the derived class. 

class Company:
    company ="Microsoft"
    country="USA"
    age = 18

    def __init__(self):
        print(f"The company name is {self.company} and country is {self.country}")
    
    def election_age(self):
        print(f"The age is must be more then {self.age} years")

class Uni(Company):
    uniname = "Lincoln"

    def uni_name(self):
        print(f"The uni name is {self.uniname}")

    def __init__(self):
        super().__init__()
        super().election_age()
    

class Employee(Uni):
    name ="Manish"
    salary="120000000"
    def __init__(self):
        super().__init__()
        super().uni_name()

b = Employee()

print(b.company)
print(b.name)
print(b.election_age())
print(b.uniname)

 