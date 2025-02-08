# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) 
# and get fare information of train running under Indian Railways. 

from random import randint

amount = randint(200, 3000)

class Train:

    def __init__(self, train_No):
        self.train_No = train_No

    def get_status(self):
        print(f"The train {self.train_No} is running on time")
    def get_fare(self, fro, to):
        print(f"The fare of train no. {self.train_No} from {fro} to {to} is {amount}")

info = Train(122345)

info.get_status()

info.get_fare("Lincoln", "London")