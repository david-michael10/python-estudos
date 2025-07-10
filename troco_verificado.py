preco = float(input("Preço unitário do produto: "))
qte = int(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))
total = preco * qte
troco = recebido - total
print()

if recebido >= total:
    print(f"TROCO = {troco:.2f}")
else:

    print(f"DINHEIRO INSUFICIENTE. FALTAM R$ {-1 * troco:.2f}")