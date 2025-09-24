word = input().strip()


word2 = word[0].upper() 
for i in range(1, len(word)):
    
    word3 = word[i]
    word2 = word2 + word3


print(word2)