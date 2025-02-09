l = [19,53,62,8,99,45   ]

# increment = 0
# for items in l:
#     print(f"The at increment {increment} is {l[increment]}")
#     increment +=1   

# for index, item in enumerate(l):
#     print(f"The item number at index {index} is {item}")

# LIST COMPREHENSIONS - normal
list1 = [1,7,12,11,22] 

sequredlist =[]

for items  in list1:
    sequredlist.append(items*items)

print(sequredlist)

# same can be done with LIST COMPREHENSIONS 
sequredlist = [i*i for i in list1]

print(sequredlist)
