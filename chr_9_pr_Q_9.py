# 9. Write a program to find out whether a file is identical & matches the content of 
# another file. 

with open("this.txt", "r") as f:
    content1 = f.read()
with open("new_this.txt", "r") as f:
    content2 = f.read()

if(content1 in content2):
    print("The content is mathces")
else:
    print("not")

