N = int(input())  # Número de casos de teste

total_cobaias = 0
total_coelhos = 0
total_ratos = 0
total_sapos = 0

for _ in range(N):
    quantia, tipo = input().split()
    quantia = int(quantia)

    total_cobaias += quantia

    if tipo == 'C':
        total_coelhos += quantia
    elif tipo == 'R':
        total_ratos += quantia
    elif tipo == 'S':
        total_sapos += quantia

# Calculando os percentuais
perc_coelhos = (total_coelhos / total_cobaias) * 100
perc_ratos = (total_ratos / total_cobaias) * 100
perc_sapos = (total_sapos / total_cobaias) * 100

# Exibindo os resultados
print(f"Total: {total_cobaias} cobaias")
print(f"Total de coelhos: {total_coelhos}")
print(f"Total de ratos: {total_ratos}")
print(f"Total de sapos: {total_sapos}")
print(f"Percentual de coelhos: {perc_coelhos:.2f} %")
print(f"Percentual de ratos: {perc_ratos:.2f} %")
print(f"Percentual de sapos: {perc_sapos:.2f} %")
