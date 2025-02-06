# Question 1 Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word ‘twinkle’. 

f = open("poems.txt","r")

content = f.read()

if "twinkle" in content:
    print("The word twinkle is exist in file")
else:
    print("The word twinkle is does not exist in file")
