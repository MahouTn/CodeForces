n = int(input())


a = 0

for i in range(n):
    p,q = list(map(int, input().split()))
    if q - 2 >= p:
        a += 1 
print(a)
