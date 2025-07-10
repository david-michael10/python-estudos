n = int(input("Quantos alunos serão digitados? "))
print()

nomes = [0 for x in range(n)]
n1 = [0 for x in range(n)]
n2 = [0 for x in range(n)]

for i in range(0,n):
    print(f"Digite nome, primeira e segunda nota do {i+1}o aluno:")
    nomes[i] = input()
    n1[i] = float(input())
    n2[i] = float(input())
    print()

print("Alunos Aprovados: ")
soma = 0
for i in range(0, n):
    soma = n1[i] + n2[i]
    if soma >= 12:
        print(nomes[i])