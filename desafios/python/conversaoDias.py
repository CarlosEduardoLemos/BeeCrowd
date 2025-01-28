# Leitura do número de dias
total_dias = int(input("Digite o número de dias: "))

# Cálculo dos anos, meses e dias
anos = total_dias // 365
total_dias %= 365
meses = total_dias // 30
dias = total_dias % 30

# Impressão do resultado
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")