n = int(input())

k=1
b = []
for i in range(n):
    a = input()
    b.append(a)
for j in range(len(b)-1):
        if b[j] != b[j+1]:
            k += 1

print(k)
    