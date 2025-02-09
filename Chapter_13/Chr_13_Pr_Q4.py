# . Write a program to filter a list of numbers which are divisible by 5. 

def division(n):
    if(n%5 == 0):
        return True
    return False

a = [1,2,3,50 b,4,5,6,10,500]

f = list(filter(division, a))
print(f)