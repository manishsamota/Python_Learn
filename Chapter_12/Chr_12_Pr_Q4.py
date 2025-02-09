# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’
# 

a = 10
b = 30
try:
  a = int(input("Enter the a : "))
  b = int(input("Enter the b : "))
  print(a/b)
except ValueError as v:
  print(v)
except ZeroDivisionError as z:
  print(z)

print("Thanks!")