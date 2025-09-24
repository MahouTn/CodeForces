k,n,w = map(int,input().split())

b = 0
for i in range(1,w+1):
    b += k*i


c = b - n

print(max(0, c))
