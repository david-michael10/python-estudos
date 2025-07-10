nome = input("Nome: ")
valor_hora = float(input("Valor por hora: "))
horas_trabalhadas = int(input("Horas trabalhadas: "))
print()

valor_total = valor_hora * horas_trabalhadas
print(f"O pagamento de {nome} é de: {valor_total:.2f}")