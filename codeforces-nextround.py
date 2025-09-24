n, k = map(int, input().split())
scores = list(map(int, input().split()))

threshold = scores[k-1]   # score of k-th participant
count = 0

for score in scores:
    if score >= threshold and score > 0:
        count += 1

print(count)