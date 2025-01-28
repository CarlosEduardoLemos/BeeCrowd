def calcular_soma(a, b):
    """Calcula a soma de dois valores inteiros."""
    return a + b

def main():
    # Solicita os valores de A e B ao usuário
    a = int(input("Digite o valor de A: "))
    b = int(input("Digite o valor de B: "))
    
    # Calcula a soma dos valores
    soma = calcular_soma(a, b)
    
    # Exibe o resultado
    print(f"SOMA = {soma}")

if __name__ == "__main__":
    main()