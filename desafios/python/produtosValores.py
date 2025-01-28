def calcular_produto(valor1, valor2):
    """Calcula o produto de dois valores inteiros."""
    return valor1 * valor2

def main():
    # Solicita os valores ao usuário
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    
    # Calcula o produto dos valores
    produto = calcular_produto(valor1, valor2)
    
    # Exibe o resultado
    print(f"PROD = {produto}")

if __name__ == "__main__":
    main()