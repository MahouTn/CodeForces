j = 0
how = int(input())


for _ in range(how) :
    a,b,c  = map(int,input().split())
    if a + b + c > 1:
        j += 1
print(j) 
    