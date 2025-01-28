def calcular_imposto(salario):
    # Calcula o imposto de renda baseado no salário
    if salario <= 2000:
        return 0.0
    elif salario <= 3000:
        return (salario - 2000) * 0.08
    elif salario <= 4500:
        return 1000 * 0.08 + (salario - 3000) * 0.18
    else:
        return 1000 * 0.08 + 1500 * 0.18 + (salario - 4500) * 0.28

def main():
    # Recebe o salário
    salario = float(input("Digite o salário: "))

    # Calcula o imposto
    imposto = calcular_imposto(salario)

    # Exibe o resultado
    if imposto == 0.0:
        print("Isento")
    else:
        print(f"R$ {imposto:.2f}")

if __name__ == "__main__":
    main()