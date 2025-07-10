n = int(input("Quantas pessoas você vai digitar? "))
nomes = [0 for x in range(n)]
idades = [0 for x in range(n)]
print()

for i in range (0,n):
    print(f"Dados da {i+1}a pessoa:")
    nomes[i] = input("Nome: ")
    idades[i] = int(input("Idade: "))
    print()

mais_velho = idades[0]
pos = 0
for i in range(1,n):
    if idades[i] > mais_velho:
        mais_velho = idades[i]
        pos = i
print(f"PESSOA MAIS VELHA = {nomes[pos]}")