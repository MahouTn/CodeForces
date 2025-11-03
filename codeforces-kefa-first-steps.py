n = int(input())

a = list(map(int, input().split()))
maxy = 1
j = 1
for i in range(1, n):
   
   if a[i] >= a[i-1]:
      j += 1
   else: j = 1
   maxy = max(maxy, j)
    
print(maxy)