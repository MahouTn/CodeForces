letters = set()
for ch in input():
    if ch.isalpha():
        letters.add(ch)

print(len(letters))