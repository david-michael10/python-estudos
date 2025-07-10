codigo = int(input("Código do produto comprado (1-5) : "))
qte = int(input("quantidade : "))
print()

total = 0
if codigo == 1:
    total = 5 * qte
elif codigo == 2:
    total = 3.50 * qte
elif codigo == 3:
    total = 4.80 * qte
elif codigo == 4:
    total = 8.90 * qte
elif codigo == 5:
    total = 7.32 * qte

print(f"Valor a pagar: R$ {total:.2f}")