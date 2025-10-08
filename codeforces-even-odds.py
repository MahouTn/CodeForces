n,k = list(map(int, input().split()))


count_odds = (n + 1) // 2

if k <= count_odds:
    result = (2 * k) - 1
elif k > count_odds:
    result = (k - count_odds) * 2


print(result)
