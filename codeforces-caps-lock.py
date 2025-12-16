n = str(input())

if n.isupper() or (n[0].islower() and n[1:].isupper() and len(n) > 1) or (len(n) == 1 and n.islower()):
    print(n.swapcase())
else:
    print(n)