# Optimized version
n = int(input())

# Use a dictionary for O(1) lookups instead of multiple if-elif statements
faces = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}

# Compute the total directly using a generator expression
result = sum(faces[input()] for _ in range(n))

print(result)
