# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

class Animals:
    pass
class Pents:
    pass
class Dog:
    @staticmethod # static method used to tell that you do not want to take self paramenter
    def bark():
        print("Bow Bow!")

d = Dog()
d.bark()