wordstring = eval(input("Enter words : "))
orderinteger = eval(input("Enter the order of words : "))
word0 = ""
word1 = ""
word2 = ""
word3 = ""
word4 = ""
result = ""
for i in range(len(wordstring)) :
    if i==0 :
        word4 = wordstring[i]
    elif i==1 :
        word3 = wordstring[i]
    elif i==2 :
        word0 = wordstring[i]
    elif i==3 :
        word2 = wordstring[i]
    elif i==4 :
        word1 = wordstring[i]
result = word0 + " " + word1 + " " +  word2 + " " + word3 + " " + word4
print(result)