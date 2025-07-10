preco = float(input("Preço unitário do produto: "))
quantidade = int(input("Quantidade comprada: "))
recebido = float(input("Dinheiro recebido: "))
print()

total = preco * quantidade
troco =  recebido - total
print(f"TROCO = {troco:.2f}")