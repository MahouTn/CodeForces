s = list(map(int, input().split()))

j = 0
s.sort(reverse=True)

for i in range(len(s)-1):
    if s[i] == s[i+1]:
        j += 1

print(j)