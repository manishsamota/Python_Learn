# class Company:
#     year=1991
#     @classmethod
#     def show(cls):
#         print(f"Company strated on {cls.year}")

# a = Company()
# a.year = 2000
# a.show()

# PROPERTY DECORATORS 

class Employee:
    a =1

    @property
    def name(self):
        return f"{self.fname} and {self.lname}"
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

    
e = Employee()
e.name = "Manish Samota"

print(e.fname, e.lname)