def determinar_quadrante(x, y):
    """Determina a localização do ponto (x, y) no plano cartesiano."""
    if x == 0 and y == 0:
        return "Origem"
    elif x == 0:
        return "Eixo Y"
    elif y == 0:
        return "Eixo X"
    elif x > 0 and y > 0:
        return "Q1"
    elif x < 0 and y > 0:
        return "Q2"
    elif x < 0 and y < 0:
        return "Q3"
    elif x > 0 and y < 0:
        return "Q4"

def main():
    x, y = map(float, input("Digite as coordenadas X e Y separadas por espaço: ").split())
    resultado = determinar_quadrante(x, y)
    print(resultado)

if __name__ == "__main__":
    main()