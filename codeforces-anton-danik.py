n = int(input())

players = input()

if len(players) != n:
    print("Error: The length of the string does not match the number of players.")
else:
    a = 0
    d = 0

    for i in range(n):
        if players[i] == "A":
            a += 1
        else:
            d += 1
    
    if a > d:
        print("Anton")
    elif a < d:
        print("Danik")
    else:
        print("Friendship")
