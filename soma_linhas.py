m = int(input("Qual a quantidade de linhas da matriz? "))
n = int(input("Qual a quantidade de colunas da matriz? "))
mat = [[0 for x in range(n)] for x in range(m)]
print()

for i in range(0,m):
    print(f"Digite os valores da {i + 1}a linha:")
    for j in range(0,n):
        mat[i][j] = float(input())
    print()

print("VETOR GERADO:")
for i in range(0,m):
    soma = 0
    for j in range(0,n):
        soma = soma + mat[i][j]
    print(soma)