n = int(input())

c = 0

tram = []
for i in range(n):
    a,b = list(map(int, input().split()))
    c = c + (b - a)
    tram.append(c)
largest_number = max(tram)
print(largest_number)
