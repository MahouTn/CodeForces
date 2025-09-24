import math
n,m,a = map(int,input().split())


p1 = math.ceil(n/a)
p2 = math.ceil(m/a)
p3 = p1 * p2
print(p3)
