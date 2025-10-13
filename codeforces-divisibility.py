t = int(input())


for i in range(t):
    a,b = map(int, input().split())
    s = 0 
    if a % b == 0:
        print(0)
    else: print(b - (a % b)) 
    
