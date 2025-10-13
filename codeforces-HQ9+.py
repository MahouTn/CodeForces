p = str(input())

a = 0
for i in range(len(p)):
    if p[i] in ["H","Q","9"]:
        a += 1
    
if a > 0 :
    print("YES")
else: print("NO")