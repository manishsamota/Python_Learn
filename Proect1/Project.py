'''
1 for snake
-1 for water
0 for gun
'''
import random
items = [1,-1,0]

random_number =random.choice(items)
computer = random_number

youin = input("Chose the key: ")

dir = {
    "s":1,
    "w": -1,
    "g":0
}

youstr =dir[youin]

reversed_dir ={1 :"Snake", -1:"Water", 0:"Gun"} 

print(f"***Computer have chose: {reversed_dir[computer]}*** \n ***and you have chose: {reversed_dir[youstr]}***")

if(computer == youstr):
    print("It's draw")
else:
    if(computer == 1 and youstr == 0):# 1
        print("You Win!")
    elif(computer == -1 and youstr ==0): #-1
        print("You Lose!")
    elif(computer ==1 and youstr == -1): # 2
        print("You Lose!")
    elif(computer==-1 and youstr ==1): #0 -2
        print("You Win!")
    elif(computer==0 and youstr==1): #1 -1
        print("You Lose!")
    elif(computer==0 and youstr==-1): #-1 1
        print("You Win!")
    else:
        print("Something went wrong!")
