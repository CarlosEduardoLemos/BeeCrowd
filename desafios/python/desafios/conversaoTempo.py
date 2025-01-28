# Leitura do tempo em segundos
total_segundos = int(input("Digite o tempo em segundos: "))

# Cálculo das horas, minutos e segundos
horas = total_segundos // 3600
total_segundos %= 3600
minutos = total_segundos // 60
segundos = total_segundos % 60

# Impressão do resultado no formato horas:minutos:segundos
print(f"{horas}:{minutos}:{segundos}")