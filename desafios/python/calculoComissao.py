# Leitura dos valores
nome_vendedor = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo: "))
total_vendas = float(input("Digite o total de vendas: "))

# Cálculo da comissão e total a receber
comissao = 0.15 * total_vendas
salario_total = salario_fixo + comissao

# Impressão do resultado
print(f"TOTAL = R$ {salario_total:.2f}")