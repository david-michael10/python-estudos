duracao = int(input("Digite a duração em segundos: "))
horas = duracao // 3600
resto_horas = duracao % 3600
minutos = resto_horas // 60
segundos = resto_horas % 60

print(f"{horas}:{minutos}:{segundos}")