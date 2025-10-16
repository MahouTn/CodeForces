n = int(input())

a = list(map(int, input().split()))[1:] 
b = list(map(int, input().split()))[1:] 

se = set(a + b)

if len(se) == n:
    print("I become the guy.")
else: print("Oh, my keyboard!")

