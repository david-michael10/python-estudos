n = int(input("Qual a ordem da matriz? "))
mat = [[0 for x in range(n)] for x in range(n)]
print()

for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))
    print()

print("DIAGONAL PRINCIPAL:")
for i in range(0,n):
    print(mat[i][i],end= " ")
print()
print()

cont = 0
for i in range(0,n):
    for j in  range(0,n):
        if mat[i][j] < 0:
            cont = cont + 1
print(f"QUANTIDADE DE NEGATIVOS = {cont}")