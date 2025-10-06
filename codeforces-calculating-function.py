n = int(input())

if n % 2 == 0:
    c = n // 2
elif n % 2 != 0:
    c = -(n + 1) // 2

print(c)