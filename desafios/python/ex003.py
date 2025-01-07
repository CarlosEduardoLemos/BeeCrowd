import math

def calcular_area_circulo(raio):
    """Calcula a área de um círculo dado o raio."""
    return math.pi * raio ** 2

def main():
    raio = float(input("Digite o valor do raio: "))
    area = calcular_area_circulo(raio)
    print(f"A={area:.4f}")

if __name__ == "__main__":
    main()