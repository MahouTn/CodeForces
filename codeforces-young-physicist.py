matrix = []
n = int(input())

x_sum = 0
y_sum = 0
z_sum = 0

for i in range(n):
    x,y,z = list(map(int,input().split()))
    matrix.append([x, y, z])

    x_sum += x
    y_sum += y
    z_sum += z

if x_sum == 0 and y_sum == 0 and z_sum == 0:
    print("YES")
else: print("NO")

