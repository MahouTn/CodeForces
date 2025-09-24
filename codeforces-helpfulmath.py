number = input().strip()

parts = number.split("+")

swapped = True

while swapped:
    swapped = False
    for i in range(len(parts)-1):
        if parts[i] > parts[i+1]:
            parts[i], parts[i+1] = parts[i+1], parts[i]
            swapped = True

result = '+'.join(parts)
print(result)
