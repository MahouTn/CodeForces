a,b = map(int, input().split())

a  = a*3
b  = b*2
i = 1
while a <= b:
    a  = a*3
    b  = b*2
    i = i+1

print(i)