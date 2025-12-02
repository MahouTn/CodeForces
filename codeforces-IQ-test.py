n = int(input())
a = list(map(int, input().split()))


l = []
p = []
for i in range(n):
    if a[i] % 2 == 0:
        l.append(i+1)
    else: p.append(i+1)

if len(l) > len(p):
    print(*p)
else: print(*l)