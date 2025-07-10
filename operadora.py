qte = int(input("Digite a quantidade de minutos: "))
pgt = 0
if qte <= 100:
    pgt = 50
    print(f"Valor a pagar: R$ {pgt:.2f}")
else:
    pgt = 50
    diferenca = (qte - 100) * 2
    valor_total = pgt + diferenca
    print(f"Valor a pagar: R$ {valor_total:.2f}")