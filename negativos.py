n = int(input("Quantos números você vai digitar? "))
print()
vet = [0 for x in range(n)]

for i in range(0,n):
    vet[i] = int(input("Digite um número: "))
print()
print("NÚMEROS NEGATIVOS: ")
for i in range(0,n):
    if vet[i] < 0:
        print(vet[i])