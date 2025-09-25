t = int(input())

for i in range(t):
    count = 0
    maximum_difference = 0
    n = int(input())
    a = list(map(int,input().split()))
    a.sort(reverse=True)
    for j in range(0, n, 2):
        count = a[j] - a[j+1]

        if count > maximum_difference:
            maximum_difference = count
    print(maximum_difference)

