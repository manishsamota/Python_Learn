# . Create a class (2-D vector) and use it to create another class representing a 3-D vector. 

class TwoDVector:
    def __init__(self, i, j):
        self.i =i
        self.j = j
    def show(self):
        print(f"The vecor is {self.i}i + {self.j}j")

class ThreeDVercor(TwoDVector):
    def __init__(self, k,i,j):
        super().__init__(i,j)
        self.k = k

    def show(self):
        print(f"The Three D vecor is = {self.i}i + {self.j}j +{self.k}k ")
    
twod = TwoDVector(2,3)
twod.show()
theeed = ThreeDVercor(6,7,9)
theeed.show()

