n = int(input("Quantos elementos vai ter o vetor? "))
vet = [0 for x in range(n)]
print()

for i in range(0,n):
    vet[i] = float(input("Digite um número: "))
print()

soma = 0
for i in range(0,n):
    soma = soma + vet[i]
media = soma / n
print(f"MÉDIA DO VETOR = {media}")

print("ELEMENTOS ABAIXO DA MÉDIA: ")
for i in range(0,n):
    if vet[i] < media:
        print(vet[i])