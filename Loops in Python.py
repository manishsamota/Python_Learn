# i = 1
# while(i<6):
#     print(i)
#     i +=1

# l = ['Manish',9, 'Baljeet', 'Jitin']
# i=0
# while(i<len(l)):
#     print(l[i])
#     i = i+1
# in the while loop we need to define the initial value of i and till when the program will run and how you want to run / increment will define inside the loop
i =0
# while(i<5):
#     print("Manish")
#     i = i+1

# l = [1,5,6,8,9,10]
# for i in l:
#     print(i)
# RANGE FUNCTION IN PYTHON 
# The range() function in python is used to generate a sequence of number. 
# We can also specify the start, stop and step-size as follows: 
# range(start, stop, step_size) 
# # step_size is usually not used with range() 
# by default the start value in range is 0 to n-1

# for i in range(9):
#     print(i)
# for i in range (2, 10): 
#     print(i)
# for i in range(2,10, 3): # in this start from 2 to 10 and gap/step with next number is 3
#     print(i)
# how to itrate / print the touple 
t =(2,5,6,10,"Manish","Rade",True)
# for i in t:# How it is running -> i will fetch the elements of touple t and print 
#     print(i)

# how to itrate / print list 

l = [2,5,8,True,10.25,"Manish"]

# for i in l: # i will fetch the list in python we do not need to define the variable 
#     print(i)

# for loop with else
# list1 = ["Manish", 2,5,True]

# for item in list1:
#     print(item)
# else:
#     print("The work is Done")
 
 # break statement 
# for i in range(10):
#     print(i)
#     if(i ==5):
#       break

 # continue statement 

# for i in range(4): 
#     print("printing") 
#     if i == 2:   # if i is 2, the iteration is skipped  
#         continue 
#     print(i)
# for i in range(10):
#     if i==5:
#         continue
#     print(i) 

#pass statement
i=0 # we must need to provide the initial value of i in  while loop
for i in  range(5):
    pass
    # print(i)
    # i=i+2 # we must need to provide the step in while loop
for item in range(10):
    print("Manish")
