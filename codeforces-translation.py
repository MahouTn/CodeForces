s = input()
t = input()

a = 0

if len(s) == len(t):
    for i in range(len(s)-1, -1, -1):
        if s[i] == t[a]:
            a += 1

if a == len(s):
    print("YES")
else: print("NO")
