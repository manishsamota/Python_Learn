#3. Write a program to generate multiplication tables from 2 to 20 and write it to the 
# different files. Place these files in a folder for a 13 – year old.

def geratetables(n):
    table =""
    # for loop from 1 to 10
    for i in range(1,11):
        # get the table and add next
        table += (f"{n} * {i} = {n*i} \n")
        # write the tables in different files 
    with open (f"Tables/table_{n}.txt","w") as f:
        f.write(table)

# for loop for generate and provide the number one by one
for i in range(2, 21):
    geratetables(i)