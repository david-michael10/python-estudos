casos = int(input("Quantos casos de teste serão digitados? "))
print()

qte_total = 0
qte = 0
c = 0
r = 0
s = 0
for i in range (0,casos):
    qte = int(input("Quantidade de cobaias: "))
    qte_total = qte_total + qte
    tipo = input("Tipo de cobaia (C/R/S): ")
    print()
    if tipo == "c":
        c = c + qte
    elif tipo == "r":
        r = r + qte
    elif tipo == "s":
        s = s + qte
print("RELATÓRIO FINAL: ")
print()

print(f"TOTAL: {qte_total} cobaias")
print(f"Total de coelhos: {c}")
print(f"Total de ratos: {r}")
print(f"Total de sapos: {s}")
print()

percentual_c = c * 100 / qte_total
print(f"Percentual de coelhos: {percentual_c:.2f}")

percentual_r = r * 100 / qte_total
print(f"Percentual de ratos: {percentual_r:.2f}")

percentual_s = s * 100 / qte_total
print(f"Percentual de sapos: {percentual_s:.2f}")