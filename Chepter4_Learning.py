friends = ["Apple", "Oragange", 5, 465, 23.23, False, "Manish", "Arun"]

print(friends)
print(friends[1])
friends [1] ="Grapes" # Unlike strings lists are mutable
print(friends[1])
print(friends[2:5])

# Method of list
friends.append("Ravi")
print(friends)

l1 = [56,31,32,16,21,1,2,31,0]
l1.sort() #increasing order
print(l1)
l1.reverse() # reverse of increasing
print(l1)

l1.insert(3,2) #insert the 41 at 3 index
print(l1)

l1.pop(1) # remove the revlaue at index 3
print(l1)

l1.remove(1) # it will remove first value of given number here that is 1
print(l1)
