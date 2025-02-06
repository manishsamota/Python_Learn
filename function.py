# #function defination
# def avg1():
#     a = int(input("Enter the number = "))
#     b = int(input("Enter the number  = "))
#     c = int(input("Enter the number  = "))
#     avgof = (a+b+c)/3
#     print(avgof)

# avg1() #function call

# def goodDay():
#     name = input("Enter your name = ")
#     print(f"Have a good day {name}")
# goodDay()

# def goodDay1(name, ending):
#     print(f"Have a Good Day {name}", end="") #end="" define that end the line but not move into new line
#     print(f"{ending} for visiting us!")
#     return "okey done"

# a = goodDay1("Manish", " Thank you")
# print(a)
# goodDay1("Anil", " Thanks")

#retun value concept

# def retun1(name):
#     gr = "Hello " + name
#     return gr

# retun_value = retun1("Manish")

# print(retun_value)

# Default agrument concept

# def defalutarg(name,ending ="Thanks you"):
#     gr =f"Welcome {name} and {ending} for visiting us!"
#     return gr

# user1 = defalutarg("Manish") # if we do not pass any value for ending then it will take bydefault value 
# user2 = defalutarg("Baljeet","Thanks") # but if we pass the value of agrument = ending then it will take this new value 
# print(user1)
# print(user2)

# recussion

# factorial of 0 = 1
# factorial of 1 = 1
# factorial of 2 = 2*1
# factorial of 3 = 3*2*1
# factorial of 4 = 4*3*2*1
# factorial of 5 = 5*4*3*2*1
# factorial of n = n* n-1 * n-2 * ... *3*2*1

# factorial of n = n* factorial(n-1)

def factorial(number):
    if number == 1 or number==0:
        return 1
    return number* factorial(number-1)

number = int(input("Enter the number = "))
total_factorial = factorial(number)
print(f"The factorial of given n number = {number} is = {total_factorial}")

