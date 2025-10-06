n = int(input())

str_n = str(n)
j = 0

list = [4,7,44,77,47,74,444,447,474,477,744,747,774,777]

for i in range(len(list)):
    if n % list[i] == 0:
        j +=1

if j >= 1:
    print("YES")
else: print("NO")