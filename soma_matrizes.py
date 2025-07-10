m = int(input("Quantas linhas vai ter cada matriz? "))
n = int(input("Quantas colunas vai ter cada matriz? "))
mat_a = [[0 for x in range(n)] for x in range(m)]
mat_b = [[0 for x in range(n)] for x in range(m)]
mat_c = [[0 for x in range(n)] for x in range(m)]
print()

print("Digite os valores da matriz A:")
for i in range(0,m):
    for j in range(0,n):
        mat_a[i][j] = int(input(f"Elemento [{i},{j}]: "))
    print()

print("Digite os valores da matriz B:")
for i in range(0,m):
    for j in range(0,n):
        mat_b[i][j] = int(input(f"Elemento [{i},{j}]: "))
    print()

for i in range(0,m):
    for j in range(0,n):
        mat_c[i][j] = mat_a[i][j] + mat_b[i][j]

print("MATRIZ SOMA:")
for i in range(0,m):
    for j in range(0,n):
        print(mat_c[i][j], end= " ")
    print()