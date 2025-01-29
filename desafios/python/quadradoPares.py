# Leitura do valor inteiro N
limite_superior = int(input("Digite um valor inteiro: "))

# Loop para calcular e imprimir o quadrado dos números pares de 2 até N
for numero in range(2, limite_superior + 1, 2):
    quadrado = numero ** 2
    print(f"{numero}^2 = {quadrado}")