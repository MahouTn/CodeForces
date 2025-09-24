n = int(input())
x = 0
for _ in range(n):
    n1 = input()
    if n1 == "++X" or n1 == "X++":
        x = x + 1
    elif n1 == "--X" or n1 == "X--":
        x = x - 1
print(x)