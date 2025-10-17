n = int(input())

a = [100,20,10,5,1]

b = 0
for i in range(len(a)):
    count = n // a[i]
    b += count           
    n = n - count * a[i] 

print(b)