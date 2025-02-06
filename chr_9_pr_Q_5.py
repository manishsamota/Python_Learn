# 5. Repeat program 4 for a list of such words to be censored. 

# This is the list of words
words = ["bad","pagal", "ganda", "Donckey"]

# open and read the file
with open ("chr_9_q_4_file.txt","r") as f:
    content = f.read()
# from words if any word find the content then it will get replace by #    
for i in words:
    content = content.replace(i, "#" * len(i))

with open("chr_9_q_4_file.txt", "w") as f:
    f.write(content)