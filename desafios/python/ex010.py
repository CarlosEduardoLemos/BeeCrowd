# Leitura dos valores
vendedor = input()
salario = float(input())
vendas = float(input())

# Cálculo da comissão e total a receber
total = salario + 0.15 * vendas

# Impressão do resultado
print(f"TOTAL = R$ {total:.2f}")
