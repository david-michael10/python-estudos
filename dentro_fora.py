x = int(input("Quantos números você vai digitar? "))

dentro = 0
fora = 0
for i in range(0,x):
    n = int(input("Digite um número: "))
    if n >= 10 and n < 20:
        dentro = dentro + 1
    else:
        fora = fora + 1
print()

print(f"{dentro} DENTRO")
print(f"{fora} FORA")