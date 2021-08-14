# https://www.urionlinejudge.com.br/judge/pt/problems/view/1048

# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
# Salário
# Percentual de Reajuste

# 0 - 400.00
# 400.01 - 800.00
# 800.01 - 1200.00
# 1200.01 - 2000.00
# Acima de 2000.00

# 15%
# 12%
# 10%
# 7%
# 4%
# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.

# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.

# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.

def calcular_e_printar(arg0: float, salario: float):
    reajuste = arg0 * salario
    novo_salario = salario + reajuste
    print(f'Novo salario: {novo_salario:.2f}')
    print(f'Reajuste ganho: {reajuste:.2f}')
    print(f'Em percentual: {arg0 * 100:.0f} %')


def main() -> None:
    salario = float(input())

    if 0 < salario <= 400:
        calcular_e_printar(0.15, salario)
    elif 400 < salario <= 800:
        calcular_e_printar(0.12, salario)
    elif 800 < salario <= 1200:
        calcular_e_printar(0.1, salario)
    elif 1200 < salario <= 2000:
        calcular_e_printar(0.07, salario)
    elif salario > 2000:
        calcular_e_printar(0.04, salario)


if __name__ == "__main__":
    main()
