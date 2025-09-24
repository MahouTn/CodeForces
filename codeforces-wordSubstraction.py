a,b = map(int, input().split())




for i in range(b):
    c = a % 10
    if c != 0 :
       a -= 1
    else: a = a // 10

print(a)