n = int(input())

a = list(map(int, input().split()))

max_index = a.index(max(a))
min_index = n - 1 - a[::-1].index(min(a))


result = max_index + (n - 1 - min_index)

if max_index > min_index:
    result -= 1

print(result)
