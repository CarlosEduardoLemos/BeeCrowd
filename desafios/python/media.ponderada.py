N = int(input())  # Lê o número de casos de teste

for _ in range(N):
    valores = list(map(float, input().split()))  # Lê os três valores e os converte para float
    media_ponderada = (valores[0] * 2 + valores[1] * 3 + valores[2] * 5) / 10  # Calcula a média ponderada
    print(f"{media_ponderada:.1f}")  # Exibe o resultado formatado com uma casa decimal
