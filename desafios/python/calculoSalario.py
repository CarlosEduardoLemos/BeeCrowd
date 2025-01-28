# Solicita o número do funcionário
numero_funcionario = int(input("Digite o número do funcionário: "))

# Solicita o número de horas trabalhadas
horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))

# Solicita o valor da hora de trabalho
valor_por_hora = float(input("Digite o valor por hora de trabalho: "))

# Calcula o salário
salario = valor_por_hora * horas_trabalhadas

# Exibe o número do funcionário e o salário
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}")