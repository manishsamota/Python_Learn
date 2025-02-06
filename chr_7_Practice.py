
# Question 1

# number1 = int(input("Enter the number for mutiplication = "))

# for i in range(1,11):
#     print(f"This number is {i}*{number1} = {i*number1}")

# Question 2

# l = ["Harry", "Soham", "Sachin", "Rahul"] 

# for name in l:
#     if name.startswith("S"): # startwith is a function for string which return the firt letter of any string
#         print(f"Hello {name}")

# Question 3

# number2 = int(input("Provide the number for mutiply = "))

# i =1

# while(i<=10):
#     print(f"{i}*{number2} = {i*number2}")
#     i+=1

# Question 3

# number3 = int(input("Enter the number = "))

# remineder = number3%2

# for i in range (2, number3):
#     if number3%i ==0:
#         print(f"The given number {number3} is not prime")
#         break
#     else:
#         print(f"The given {number3} is prime ")
#         break


# Question 5 - Write a program to find the sum of first n natural numbers using while loop. 

# number5 = int(input("Enter the number = "))
# i=0
# sum =0
# while(i<=number5):
#     sum = sum+i
#     i = i+1
# print(sum)

# Question - 6 - Write a program to calculate the factorial of a given number using for loop. 
# number6 = int(input("Enter the number = "))
# fact = 1
# for i in range (number6,0,-1): # by default the step is +1, to inverse it we need to define it as -1 
#     fact = fact*i
# print(fact)

# Question 7  
# Write a program to print the following star pattern. 
# * 
# *** 
# ***** for n = 3
# 
 
# number7 = int(input("Enter the number = "))
# for i in range(0,number7+1):
#     #create the space
#     print(" "* (number7-i), end="")
#     print("*"*(2*i-1), end="")
#     print("")

# Question 8 Write a program to print the following star pattern: 
# * 
# ** 
# ***      for n = 3 

# number8 = int(input("Enter the number = "))

# for i in range(number8+1):
#     print("*" * i, end="")
#     print("")

# Question 9. Write a program to print the following star pattern. 
# * * * 
# *   *   for n = 3 
# * * *  

# number9 = int(input("Enter the number = "))

# for i in range(number9+1):
#    if(i==1 or i==number9):
#       print("*"*number9, end="")
#    else:
#       print("*",end="")
#       print(" "* (number9-2) ,end="")
#       print("*", end="")
#    print("")


# 10. Write a program to print multiplication table of n using for loops in reversed order. 

number10 = int(input("Enter the number = "))

for i in range(number10, 0, -1):
    print(f"{i}*{number10} = {i*number10}")    
