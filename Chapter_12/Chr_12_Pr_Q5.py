# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 

n  = int(input("Enter the number : "))

table = [ n*i for i in range(1,11) ]


print(table)

with open("new.txt", "a") as f:
    f.write(str(table) + "\n")
    
