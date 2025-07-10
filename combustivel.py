mensagem = 0
alcool = 0
gasolina = 0
diesel = 0
while mensagem != 4:
    mensagem = int(input("Informe um código (1, 2, 3) ou 4 para parar: "))
    if mensagem == 1:
        alcool = alcool + 1
    elif mensagem == 2:
        gasolina = gasolina + 1
    elif mensagem == 3:
        diesel = diesel + 1

print()
print("MUITO OBRIGADO!")

print(f"Álcool = {alcool}")
print(f"Gasolina = {gasolina}")
print(f"Diesel = {diesel}")