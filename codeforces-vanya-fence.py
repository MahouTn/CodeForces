n,h = list(map(int, input().split()))
a = list(map(int, input().split()))


b = 0
for i in range(n):
    if a[i] <= h:
        b += 1
    else: b +=2
print(b)