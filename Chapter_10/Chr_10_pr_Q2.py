#2. Write a class “Calculator” capable of finding square, cube and square root of a number. 

class Calculator:
    # to take the parameters i need to define constructors
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The cube is  {self.n*self.n*self.n}")
    def square_root(self):
        print(f"The square root of number is = {self.n**1/2}")

obj = Calculator(4)

obj.square()

obj.cube()

obj.square_root()