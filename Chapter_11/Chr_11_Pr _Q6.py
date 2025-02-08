# Write __str__() method to print the vector as follows: 
# 7i + 8j +10k  
# Assume vector of dimension 3 for this problem. 

# 5. Write a class vector representing a vector of n dimensions. Overload the + and * 
# operator which calculates the sum and the dot(.) product of them.


class Vector:
    def __init__(self, x, y, z):
        # Initialize the vector with any number of dimensions
        self.x =x
        self.y = y
        self.z = z
        
    def __add__(self, other):
        # Overload the + operator to add two vectors element-wise
        result  = Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        return result
    
    def __mul__(self, other):
        result =  self.x * other.x + self.y * other.y + self.z * self.z
        return result
    
    def __str__(self):
        return f"Vector ({self.x}i, {self.y}j, {self.z}k)"

# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

# Vector addition
print(v1 + v2)  # Output: (5, 7, 9)

# Dot product
print(v1 * v2)  # Output: 32 (1*4 + 2*5 + 3*6)

