# Leitura do valor inteiro X
valor_inicial = int(input("Digite um valor inteiro: "))

# Ajuste para o próximo número ímpar, se necessário
if valor_inicial % 2 == 0:
    valor_inicial += 1

# Loop para imprimir os próximos 6 números ímpares
for _ in range(6):
    print(valor_inicial)
    valor_inicial += 2