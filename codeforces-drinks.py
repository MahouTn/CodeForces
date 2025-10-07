n = int(input())

p = list(map(int, input().split()))


result = 0
for i in range(len(p)):
    result += p[i] 

print(result/n)