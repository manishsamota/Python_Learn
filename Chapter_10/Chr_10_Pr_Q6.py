# 6. Can you change the self-parameter inside a class to something else (say 
# “manish”). Try changing self to “slf” or “manish” and see the effects.

from random import randint

amount = randint(200, 3000)

class Train:

    def __init__(manish, train_No):
        manish.train_No = train_No

    def get_status(manish):
        print(f"The train {manish.train_No} is running on time")
    def get_fare(manish, fro, to):
        print(f"The fare of train no. {manish.train_No} from {fro} to {to} is {amount}")

info = Train(122345)

info.get_status()

info.get_fare("Lincoln", "London")