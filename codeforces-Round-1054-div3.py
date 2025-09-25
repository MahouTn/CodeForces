t = int(input())

for i in range(t):
    zeros_count = 0
    negatives_count = 0
    n = int(input())
    a = list(map(int,input().split()))
    for j in a:
        if j == 0:
            zeros_count += 1
        elif j == -1:
            negatives_count += 1
    total_operations = zeros_count
    if negatives_count % 2 != 0:
        total_operations += 2

    print(total_operations)
