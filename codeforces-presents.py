n = int(input())
p = list(map(int,input().split()))

c = [0] * n # Initializes a list of n zeros

for i in range(n):
    a = p[i] - 1
    b = i + 1
    c[a] = b
        
print(*c)