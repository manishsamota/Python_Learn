# Walrus operator

# if(n:= len([1,2,3,4,5])) > 2:
#     print(f"List is too long {n}, elements, Expected <= 3")

# # we can write the above proram as given below 
# # it is just assigning the vaule and comparing it same time means it is doing two things at a time

# # l = [1,2,3,4,5]
# # n = len(l)
# # if(n > 3):
# #     print(f"Len of list is {n} and it is greater then given number")
# else:
#     print("Condition not match")

# TYPES DEFINITIONS IN PYTHON 

age: int  = 25

#function type hints

def greetings(name: str) -> str:
    return f"Hello {name} !"


print(greetings("Manish"))