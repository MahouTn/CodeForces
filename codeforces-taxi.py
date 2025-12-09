n = int(input())
groups = list(map(int, input().split()))

count = [0] * 5
for i in groups:
    count[i] += 1

taxis = 0

taxis += count[4]

pairs = min(count[3], count[1])
taxis += pairs
count[3] -= pairs
count[1] -= pairs

taxis += count[3]

taxis += count[2] // 2
count[2] %= 2

if count[2]:
    taxis += 1
    count[1] = max(0, count[1] - 2)

taxis += (count[1] + 3) // 4

print(taxis)