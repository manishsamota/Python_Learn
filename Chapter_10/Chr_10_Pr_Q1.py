# Create a class “Programmer” for storing information of few programmers working at Microsoft. 

class micro:
    company ="Microsoft"

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary


Manish = micro("Manish", 23, 120000000)
print(Manish.name, Manish.age, Manish.salary)

Ravi = micro("Ravi", 24, 12000000)
print(Ravi.name, Ravi.age, Ravi.salary)