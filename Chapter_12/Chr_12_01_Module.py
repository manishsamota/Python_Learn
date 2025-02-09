def myfun():
    print("This is simple function of Module")

myfun()

filename = __name__
print(filename)

if(filename == "__main__"):
    print("This is extra code")
