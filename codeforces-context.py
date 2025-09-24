def solve():
    n = int(input())
    p = list(map(int, input().split()))

    idx_n = 0
    for i in range(n):
        if p[i] == n:
            idx_n = i
            break
    
    is_increasing = True
    for i in range(1, idx_n + 1):
        if p[i] <= p[i-1]:
            is_increasing = False
            break

    is_decreasing = True
    for i in range(idx_n + 1, n):
        if p[i] >= p[i-1]:
            is_decreasing = False
            break

    if is_increasing and is_decreasing:
        print("YES")
    else:
        print("NO")

t = int(input())
for _ in range(t):
    solve()