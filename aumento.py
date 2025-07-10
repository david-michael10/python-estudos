salario = float(input("Digite o salário da pessoa: "))

if salario <= 1000:
    percentual = 20
    porcentagem = 20 / 100 * salario
    novo_sal = salario + porcentagem
    aumento = novo_sal - salario
elif salario <= 3000:
    percentual = 15
    porcentagem = 15 / 100 * salario
    novo_sal = salario + porcentagem
    aumento = novo_sal - salario
elif salario <= 8000:
    percentual = 10
    porcentagem = 10 / 100 * salario
    novo_sal = salario + porcentagem
    aumento = novo_sal - salario
else:
    percentual = 5
    porcentagem = 5 / 100 * salario
    novo_sal = salario + porcentagem
    aumento = novo_sal - salario

print(f"Novo Salário = {novo_sal:.2f}")
print(f"Aumento = {aumento:.2f}")
print(f"Porcentagem = {percentual} %")