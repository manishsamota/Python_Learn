# square = lambda x:x*x 
# print(square(6))  # returns 36 
# sum = lambda a,b,c:a+b+c 

# a  =["Manish", "Ravi", "Shubham"]

# final = "&&<<>>MMWW".join(a)
# print(final)


# FORMAT METHOD (STRINGS)
# a = "{} is a good {}".format("Manish", "Boy")

# print(a)
# b = "{} is a good {}".format("Narayan", "Boy") # this is defalut which is same as just below 
# print(b)
# b = "{0} is a good {1}".format("Narayan", "Boy")
# print(b)
# b = "{1} is a good {0}".format("Narayan", "Boy")
# print(b)

#map example

# l = [1,2,3,4,5,6]
# sequre = lambda a: a*a

# sqList = map(sequre, l)
# print(list(sqList))


# filter example

# l = [1,2,3,4,5,6]
# def even(n):
#    if(n%2==0):
#       return True
#    return False

# onlyEven = filter(even, l)
# print(list(onlyEven))


# Reduce Fun Example

from functools import reduce
l = [1,2,3,4,5,6]
def sum(a, b):
    return a +b

# lembda function

mul = lambda a,b : a*b

print(reduce(sum, l))

print(reduce(mul, l))