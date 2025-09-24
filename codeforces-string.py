string = input().strip()
string2 = input().strip()

if string.casefold() == string2.casefold():
    print("0")
elif string.casefold() < string2.casefold():
    print("-1")
else:
    print("1")