def calcular_diferenca(a, b, c, d):
    """Calcula a diferença do produto de A e B pelo produto de C e D."""
    return a * b - c * d

def main():
    # Solicita os valores ao usuário
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    c = int(input("Digite o valor de C: "))
    d = int(input("Digite o valor de D: "))
    
    # Calcula a diferença
    diferenca = calcular_diferenca(a, b, c, d)
    
    # Exibe o resultado
    print(f"DIFERENCA = {diferenca}")

if __name__ == "__main__":
    main()