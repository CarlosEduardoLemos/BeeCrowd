import math

# Leitura das coordenadas do primeiro ponto
x1, y1 = [float(coordenada) for coordenada in input("Digite as coordenadas do primeiro ponto (x1 y1): ").split(' ')]

# Leitura das coordenadas do segundo ponto
x2, y2 = [float(coordenada) for coordenada in input("Digite as coordenadas do segundo ponto (x2 y2): ").split(' ')]

# Cálculo da distância entre os dois pontos
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Impressão do resultado
print(f"Distância entre os pontos: {distancia:.4f}")