# a = int(input("Enter the value of a: "))
# b= int(input("Enter the value of b: "))

# try:
#     a = int(input("Enter the value of a: "))
#     b= int(input("Enter the value of b: "))

# except ValueError as v:
#     print(v)

# except Exception as e:
#     print(e)


# if (b==0):
#     raise ZeroDivisionError("You can not enter the zero ")

# else:
#     print(f"The divison of a by b is: {a/b}")

# Finally word - this will run whatevery 

def main():
    try:
        a= int(input("Enter a number : "))
        print(a)
        return
    
    except ValueError as v:
        print(v)
        print("This is value error")
        return
    
    except Exception as e:
        print(e)
        print("This is exception error")
        return
    
    finally:
        print("Hey, I am in finally!")

main()
