n = int(input("enter max string length (N): "))
s = input()

s = s[:n]

# If you run your code with:
# n = 10
# s = "The quick brown fox jumps" (Length 27)

# The line s = s[:n] will change s to:
# "The quick " (Length 10)

s = s.lower()
x = set(s)

if len(x) >= 26:
    print("YES")
else: print("NO")