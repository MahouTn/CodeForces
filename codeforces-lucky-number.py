n = int(input())


a = 0
n_str = str(n)
for i in range(len(n_str)):
    if n_str[i] == "4" or n_str[i] == "7":
        a += 1
    
if a == 4 or a == 7:
    print("YES")
else: print("NO")