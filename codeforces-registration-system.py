n = int(input())
db = {}

for _ in range(n):
    name = input()

    if name not in db:
        db[name] = 0
        print("OK")
    else:
        db[name] += 1
        print(f"{name}{db[name]}")