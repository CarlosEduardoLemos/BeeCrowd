# Leitura do tempo gasto na viagem (em horas)
tempo_viagem = int(input("Digite o tempo gasto na viagem (em horas): "))

# Leitura da velocidade média durante a viagem (em km/h)
velocidade_media = int(input("Digite a velocidade média durante a viagem (em km/h): "))

# Cálculo da distância percorrida
distancia_percorrida = tempo_viagem * velocidade_media

# Cálculo da quantidade de combustível gasto (considerando 12 km/l)
combustivel_gasto = distancia_percorrida / 12

# Impressão do resultado
print(f"Combustível gasto: {combustivel_gasto:.3f} litros")