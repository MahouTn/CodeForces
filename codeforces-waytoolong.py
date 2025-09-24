n = int(input())


for _ in range(n):
    k = input()
    if len(k) > 10:
        k1 = k[0] + str(len(k)-2) + str(k[-1])
        print(k1)
    else:
        print(k)
