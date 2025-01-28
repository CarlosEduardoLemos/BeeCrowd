def calcular_percentual_reajuste(salario):
    # Determina o percentual de reajuste com base no salário
    if salario <= 400.00:
        return 15
    elif salario <= 800.00:
        return 12
    elif salario <= 1200.00:
        return 10
    elif salario <= 2000.00:
        return 7
    else:
        return 4

def calcular_reajuste(salario, percentual):
    # Calcula o valor do reajuste e o novo salário
    reajuste = salario * percentual / 100
    novo_salario = salario + reajuste
    return novo_salario, reajuste

def main():
    # Entrada do salário do funcionário
    salario = float(input("Digite o salário do funcionário: "))

    # Calcula o percentual de reajuste
    percentual = calcular_percentual_reajuste(salario)

    # Calcula o reajuste e o novo salário
    novo_salario, reajuste = calcular_reajuste(salario, percentual)

    # Exibe os resultados
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual} %")

if __name__ == "__main__":
    main()