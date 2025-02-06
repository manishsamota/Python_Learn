# # Question 1 Write a program to read the text from a given file ‘poems.txt’ and find out 
# # whether it contains the word ‘twinkle’. 

# f = open("poems.txt","r")

# content = f.read()

# if "twinkle" in content:
#     print("The word twinkle is exist in file")
# else:
#     print("The word twinkle is does not exist in file")

# 2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score.
# import random

# def game():
#     #random and randint will generate the intiger number between 1 to 100
#     score = random.randint(1,100)
#     #fecth the high score
#     with open("Hi-score.txt", "r") as f:
#         hisocre = f.read()
#         # if file is not blank then fecth the value what it have
#         if(hisocre !=""):
#             hisocre = int(hisocre)
#         # if is do not have any value then high score will be 0
#         else:
#             hisocre=0
#     print(f"Your score is {score}")
#     #comparering the random generated score and already exit score
#     if(score>hisocre):
#         with open("Hi-score.txt","w") as f:
#             f.write(str(score))
#     return score

# game()



