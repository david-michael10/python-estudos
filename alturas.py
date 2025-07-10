n = int(input("Quantas pessoas serão digitadas? "))
nomes = [0 for x in range(n)]
idades = [0 for x in range(n)]
alturas = [0 for x in range(n)]
print()

for i in range(0,n):
    print(f"Dados da {i+1}a pessoa: ")
    nomes[i] = input("Nome: ")
    idades[i] = int(input("Idade: "))
    alturas[i] = float(input("Altura: "))
    print()

soma = 0
for i in range(0,n):
    soma = soma + alturas[i]
media = soma / n
print(f"Altura Média = {media:.2f}")

cont = 0
for i in range(0, n):
    if idades[i] < 16:
        cont = cont + 1
menos_16 = cont * 100 / n
print(f"Pessoas com menos de 16 anos = {menos_16:.1f}%")

for i in range(0,n):
    if idades[i] < 16:
        print(nomes[i])