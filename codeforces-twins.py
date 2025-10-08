n = int(input())
p = list(map(int, input().split()))
p.sort(reverse=True)

sum = 0
for i in range(n):
    sum = sum + p[i]
a = 0
coin = 0
sum_me = sum / 2
for j in range(n):
    a = a + p[j]
    coin += 1
    if a > sum_me:
        break
        

print(coin)
        

