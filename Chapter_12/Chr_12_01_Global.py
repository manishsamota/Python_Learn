a = 20

def fun():
    global a

    a=30

    print(f"The value of a = {a}")

fun()
print(a)
