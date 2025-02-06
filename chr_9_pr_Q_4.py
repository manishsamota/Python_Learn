# . A file contains a word “Donkey” multiple times. You need to write a program 
# which replace this word with ##### by updating the same file.


with open("chr_9_q_4_file.txt", "r") as f:
    data = f.read()
# replace is the function in python which replace the any word with respective word
removeword = data.replace("Donkey", "######")

with open("chr_9_q_4_file.txt", "w") as f:
    f.write(removeword)
