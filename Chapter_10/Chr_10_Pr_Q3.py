# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 

class Three:
    a =15
obj = Three()

obj.a = 0 # set the instance attribute

print(f"{obj.a} but {Three.a}")