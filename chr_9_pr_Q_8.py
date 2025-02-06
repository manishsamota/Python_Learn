# 8. Write a program to make a copy of a text file “this. txt” 

with open("this.txt", "r") as f:
    # read the file content in content variable
    content = f.read()

with open("new_this.txt","w") as f: #create the file and write into this 
    #write the file with contenct variable as above
    f.write(content)