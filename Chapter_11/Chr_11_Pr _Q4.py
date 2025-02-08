class Complex:
    def __init__(self, r, i):
        self.r = r  # real part
        self.i = i  # imaginary part

    def __add__(self, c2):
        # Adding two complex numbers: (a + bi) + (c + di) = (a + c) + (b + d)i
        return Complex(self.r + c2.r, self.i + c2.i)

    def __mul__(self, c2):
        # Multiplying two complex numbers: (a + bi) * (c + di) = (ac - bd) + (ad + bc)i
        real_part = self.r * c2.r - self.i * c2.i
        imag_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part, imag_part)

    def __str__(self):
        # String representation for printing the complex number
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1, 2)
c2 = Complex(3, 4)

# Print the sum and product of the complex numbers
print(c1 + c2)  # Output should be 4 + 6i
print(c1 * c2)  # Output should be -5 + 10i
