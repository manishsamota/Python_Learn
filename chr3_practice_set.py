name = input("Enter your name = ")
date = input("Enter date = ")

print(f"Good Afternoon {name}") # this is called fstring 


letter = f"Dear {name} \nYou are selected!\n" +date

print(letter)

newletter = '''Dear <|Name|>,
You are selected!
<|Date|>'''

print(newletter.replace("<|Name|>", name).replace('<|Date|>',date))