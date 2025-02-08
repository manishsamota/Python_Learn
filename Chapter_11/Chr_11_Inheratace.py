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

class Company:
    company ="Microsoft"
    country="USA"

class Uni(Company):
    uni_name = "Lincoln"

class Employee(Uni):
    name ="Manish"
    salary="120000000"

b = Employee()

print(b.company)
print(b.name)
print(b.uni_name)
