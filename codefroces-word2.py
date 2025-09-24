word = input().strip()

c = 0
d = 0
for i in range(len(word)):
    if word[i] == word[i].lower():
        c += 1
    else: d += 1

if c == d:
    print(word.lower())
elif c > d:
    print(word.lower())
else: print(word.upper())
