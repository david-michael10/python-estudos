print("Digite 2 números inteiros: ")
x = int(input())
y = int(input())

troca = 0
if x < y:
    troca = x
    x = y
    y = troca

if x % y == 0:
    print("São múltiplos")
else:
    print("Não são múltiplos")