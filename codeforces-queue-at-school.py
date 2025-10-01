n,t = map(int, input().split())
s = list(input())

for j in range(t):
    i = 0
    while i <= len(s) - 2:
        if s[i] == "B" and s[i+1] == "G":
            s[i] = "G"
            s[i+1] = "B"   
            i += 2
        else: i += 1   

a = "".join(s)     

print(a)