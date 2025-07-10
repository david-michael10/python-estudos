n = int(input("Quantos números vai ter o vetor? "))
vet = [0 for x in range(n)]
print()

for i in range(0, n):
    vet[i] = int(input("Digite um número: "))
print()

soma = 0
cont = 0
for i in range(0,n):
    if vet[i] % 2 == 0:
        soma = soma + vet[i]
        cont = cont + 1
if cont != 0:
    media = soma / cont
    print(f"MÉDIA DOS PARES = {media}")
else:
    print("NENHUM PAR")