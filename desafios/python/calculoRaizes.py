import math

# Leitura dos coeficientes a, b e c
a, b, c = [float(x) for x in input("Digite os valores de a, b e c separados por espaço: ").strip().split(' ')]

# Cálculo do delta
delta = b * b - 4 * a * c

# Verificação das condições e cálculo das raízes
if a != 0 and delta >= 0:
    R1 = (-b + math.sqrt(delta)) / (2 * a)
    R2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"R1 = {R1:.5f}")
    print(f"R2 = {R2:.5f}")
else:
    print("Impossivel calcular")