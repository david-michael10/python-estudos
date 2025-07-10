inicial = int(input("Hora inicial: "))
final = int(input("Hora Final: "))

duracao_jogo = 0
if inicial > final:
    duracao_jogo = 24 - inicial + final
elif inicial == final:
    duracao_jogo = 24
else:
    duracao_jogo = final - inicial

print(f"O JOGO DUROU {duracao_jogo} HORA(S)")