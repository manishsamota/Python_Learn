# Question 1
# num1 = int(input('Enter the number 1 = '))
# num2 = int(input('Enter the number 2 = '))
# num3 = int(input('Enter the number 3 = '))
# num4 = int(input('Enter the number 4 = '))

# if(num1>num2 and num1>num3 and num1>num4):
#     print("Number 1 is grateset = ",num1)
# elif(num2>num1 and num2>num3 and num2> num4):
#     print("Number 2 is gretest = ", num2)
# elif(num3>num1 and num3>num2 and num3> num4):
#     print("Number 3 is greatest = ", num3)
# else:
#     print("Number 4 is greatest = ", num4)

# Question 2
# sub1_mark = int(input("Enter the 1 sub number = "))
# sub2_mark = int(input("Enter the 2 sub number = "))
# sub3_mark = int(input("Enter the 3 sub number = "))

# total_numer = sub1_mark+sub2_mark+sub3_mark

# percetage = 100*(total_numer)/300

# if(percetage>40 and sub1_mark>=33 and sub2_mark>=33 and sub3_mark>=33):
#     print(f"Congratulation you are passed with {percetage} % ")
# else:
#     print("You are faild, try harder!")

# # Question 3
# p1 = "Make a lot of money"
# p2 = "buy now"
# p3 = "subscribe this"
# p4 = "click this"
# word = ["Make a lot of money", "buy now", "subscribe this", "click this"]

# send = input("Enter the comment = ")

# if ((p1 in send) or (p2 in send)  or (p3 in send )or (p4 in send )):
#     print("This comment is a spam")
# else:
#     print("This comment is not a spam")

# Question 4

# chr =  input("Enter the username = ")

# if (len(chr)<10):
#     print("This is less then 10 chr")
# else:
#     print("This is more then 10 chr")

# #Question 5
# list = ["Manish", "Veer", "Tara"]

# take = input("Enter the name = ")

# if take in list:
#     print("Name exit in list")
# else:
#     print("Name do not exit in list")

# Question 6

# marks = int(input("Enter the marks = "))
 
# if(marks >= 90 and marks <= 100):
#     print(f"Ex {marks}")
# elif(marks >=80 and marks <= 90):
#     print(f"A {marks}")
# elif(marks >=70 and marks <= 80):
#     print(f"B {marks}")
# elif(marks >=60 and marks <= 70):
#     print(f"C {marks}")
# elif(marks >=50 and marks <= 60):
#     print(f"D {marks}")
# else:
#     print(f"F {marks}")

# Question 7

post = "Manish is a great boy and he help everyone and he is very well focus"

if("manish".lower() in post.lower()):
    print("Yes it in post")
else:
    print("It do not exit in post")