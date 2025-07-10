n = int(input("Qual a ordem da matriz? "))
mat = [[0 for x in range(n)] for x in range(n)]
print()

for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = float(input(f"Elemento [{i},{j}]: "))
    print()

soma = 0
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]
print(f"SOMA DOS POSITIVOS = {soma}")
print()

linha = int(input("Escolha uma linha: "))
print()
print("LINHA ESCOLHIDA: ", end= " ")
for j in range(0,n):
    print(mat[linha][j], end= " ")
print()
print()

coluna = int(input("Escolha uma coluna: "))
print()
print("COLUNA ESCOLHIDA: ", end= " ")
for i in range(0,n):
    print(mat[i][coluna], end= " ")
print()
print()

print("DIAGONAL PRINCIPAL: ", end= " ")
for i in range(0,n):
    print(mat[i][i], end= " ")
print()
print()

print("MATRIZ ALTERADA:")
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] < 0:
            print(mat[i][j] ** 2,end= " ")
        else:
            print(mat[i][j], end= " ")
    print()