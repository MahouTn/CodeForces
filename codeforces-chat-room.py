s = input()

x = "hello"
b = 0
for i in range(len(s)):
    if b < len(x) and x[b] == s[i]:
        b += 1

if b == len(x):
    print("YES")
else: print("NO")


        



