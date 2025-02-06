# #open is used to open the file
# file = open("10_file.txt") 
# #read is used to read the file
# data = file.read()
# # all file content is get read and stored in data variable then we print it
# print(data)
# #close is used to close the file
# file.close()

# WRITE FILES IN PYTHON 

# file = open("newfile.txt", "w")

# # write function is used to write the file
# file.write("I am writting the file first time")


# file.close()


# with statement

# #with statement open the file and close the file automatically 
# with open("10_file.txt","r") as file:
#     #read the file with read function and print it
#     print(file.read())

# # with statement open the file and close automatically here in variable f 
# with open("10_file.txt") as f:
#     # opened file in variable f is get read and strored data in text variable
#     text = f.read()
#     # stored file data in text varile get print using print function 
#     print(text)

# f = open("10_file.txt")

# line1 = f.readline()
# print(line1, type(line1))

# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# line4 = f.readline()
# print(line4, type(line4))

# f.close()

# f = open("10_file.txt")
# line = f.readline()
# #read the lines untill it's have text
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()


# # append the string in file 

# f = open("10_file.txt", "a+")

# str = "\nI am Manish and doing well in my life"

# f.write(str)

