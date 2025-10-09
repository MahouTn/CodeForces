s = list(map(int, input()))
x = list(map(int, input()))


result = []

for i in range(len(s)):
    if s[i] == 1 and x[i] == 1:
        result.append(0)     
    else: 
        a = s[i] + x[i]
        result.append(a)
        
output = "".join(map(str, result))
print(output)
        