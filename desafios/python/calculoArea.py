# Definição da constante PI
PI = 3.14159

# Leitura dos valores de A, B e C
A, B, C = [float(x) for x in input("Digite os valores de A, B e C separados por espaço: ").split(' ')]

# Cálculo das áreas
area_triangulo = (A * C) / 2
area_circulo = PI * C * C
area_trapezio = ((A + B) / 2) * C
area_quadrado = B * B
area_retangulo = A * B

# Impressão dos resultados
print(f"TRIANGULO: {area_triangulo:.3f}")
print(f"CIRCULO: {area_circulo:.3f}")
print(f"TRAPEZIO: {area_trapezio:.3f}")
print(f"QUADRADO: {area_quadrado:.3f}")
print(f"RETANGULO: {area_retangulo:.3f}")