# Read the number of rows
n = int(input())
# Read the matrix
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)


# Count how many times a first column value appears in the second column of any row
count = 0
for i in range(n):
    home = matrix[i][0]
    for j in range(n):
        guest = matrix[j][1]
        if home == guest:
            count += 1

print(matrix[j][0])
print(matrix[i][0])
print(count)
