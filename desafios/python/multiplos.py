def ler_valores():
    # Lê dois valores inteiros e retorna-os como uma tupla
    return map(int, input("Digite dois valores inteiros separados por espaço: ").split())

def sao_multiplos(A, B):
    # Verifica se A e B são múltiplos
    return A % B == 0 or B % A == 0

def main():
    # Entrada de dois valores inteiros A e B
    A, B = ler_valores()

    # Verifica se são múltiplos e exibe o resultado
    if sao_multiplos(A, B):
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")

if __name__ == "__main__":
    main()