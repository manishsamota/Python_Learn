# #Qustion  1. Write a program using functions to find greatest of three numbers. 

# def greatest(a,b,c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     else:
#         return c
    

# a =50
# b=60
# c=70
# great = greatest(a,b,c)
# print(f"The greatest number is {great}")

# Question : 2. Write a python program using function to convert Celsius to Fahrenheit. 


# def f_c(f):
#     c = 5*(f-32)/9
#     return c


# f = int(input("Enter the temp in fahrenheit = "))

# temp_C = f_c(f)
# print(f"Temprature in calcius is: {temp_C}")

# Question 3. How do you prevent a python print() function to print a new line at the end. 

# print("a")
# print("b")
# print("c", end="")
# print("d")

# Question 4. Write a recursive function to calculate the sum of first n natural numbers. 

# def n_sum(number):
#     if number ==1:
#         return 1
#     elif number ==0:
#         return 0
#     total = number + n_sum(number-1)
#     return total
# in_nu = int(input("Enter the number = "))

# sum = n_sum(in_nu)
# print(sum)


# Question 5. Write a python function to print first n lines of the following pattern: 
# *** 
# **               
# * - for n = 3 

# def print_Start(n):
#     if(n ==0):
#         return
#     print("*" * n)
#     print_Start(n-1)

# print_Start(5)

# Question 6. Write a python function which converts inches to cms. 

# def inch_cm(inch):
#     cm  = inch*2.54
#     return cm

# number1 = int(input("Enter the inch = "))

# print(f"The corssponding cm is = {inch_cm(number1)}")


# 7. Write a python function to remove a given word from a list ad strip it at the same 
# time. 

# def rem(l, word):
#     n =[]
#     for item in l:
#         if not(item==word):
#             n.append(item.strip(word))
#     return n

# list1 =  ["Manish","Rohan", "Shubham", "an"]

# print(rem(list1, "an"))

# Question 8. Write a python function to print multiplication table of a given number. 

def mul(number):
    for i in range(1, 11):
        print(f"{i}*{number} =  {i*number}")


{mul(5)}

