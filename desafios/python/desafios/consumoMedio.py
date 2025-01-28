# Leitura da distância total percorrida (em km)
distancia_percorrida = int(input("Digite a distância total percorrida (em km): "))

# Leitura do total de combustível gasto (em litros)
combustivel_gasto = float(input("Digite o total de combustível gasto (em litros): "))

# Cálculo do consumo médio
consumo_medio = distancia_percorrida / combustivel_gasto

# Impressão do resultado
print(f"{consumo_medio:.3f} km/l")