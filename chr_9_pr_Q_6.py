# 6. Write a program to mine a log file and find out whether it contains ‘python’. 

# with open("G:\Python_Learn\log.txt", "r") as f:
#     data = f.read()

# if("Python" in data):
#     print("Yes it does contains the word")
# else:
#     print("It does not contains the word")

# 7. Write a program to find out the line number where python is present from ques 6. 

with open("log.txt", "r") as f:
    lines = f.readlines()
increment = 1
for no_lines in lines:
    if("python" in no_lines):
        print(f"The number of line is {increment}")
        break
    increment+=1
else:
    print("No python is not find in the log file")