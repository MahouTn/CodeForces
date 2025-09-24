vowel = "eyaoui"

a = input()
b = ""
for i in range(len(a)):
    if a[i].lower() not in vowel:
        b = b + "." + a[i]

print(b.lower())