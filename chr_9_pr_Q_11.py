# 11. Write a python program to rename a file to “renamed_by_ python.txt. 

with open("this.txt", "r") as f:
    content =f.read()

with open("new_file_this.txt", "w") as f:
    f.write(content)
