# A empresa ABC resolveu conceder um aumento de salários a seus funcionários de acordo com a tabela abaixo:
#
# SALÁRIO                 PERCENTUAL DE REAJUSTE
# 0 - 400.00                             15%
# 400.01 - 800.00                    12%
# 800.01 - 1200.00                  10%
# 1200.01 - 2000.00                 7%
# Acima de 2000                       4%
#
# Leia o salário do funcionário e calcule e mostre o novo salário, bem como o valor de reajuste ganho e o índice reajustado, em percentual.
#
# Entrada
# A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
#
# Saída
# Imprima 3 linhas na saída: o novo salário, o valor ganho de reajuste e o percentual de reajuste ganho, conforme exemplo abaixo.
salario = float(input())

if 0 < salario <= 400:
    reajuste = 0.15 * salario
    nsalario = salario + reajuste
    print('Novo salario: {:.2f}' .format(nsalario))
    print('Reajuste ganho: {:.2f}' .format(reajuste))
    print('Em percentual: 15 %')

elif 400 < salario <= 800:
    reajuste = 0.12 * salario
    nsalario = salario + reajuste
    print('Novo salario: {:.2f}' .format(nsalario))
    print('Reajuste ganho: {:.2f}' .format(reajuste))
    print('Em percentual: 12 %')

elif 800 < salario <= 1200:
    reajuste = 0.1 * salario
    nsalario = salario + reajuste
    print('Novo salario: {:.2f}' .format(nsalario))
    print('Reajuste ganho: {:.2f}' .format(reajuste))
    print('Em percentual: 10 %')

elif 1200 < salario <= 2000:
    reajuste = 0.07 * salario
    nsalario = salario + reajuste
    print('Novo salario: {:.2f}' .format(nsalario))
    print('Reajuste ganho: {:.2f}' .format(reajuste))
    print('Em percentual: 7 %')

elif salario > 2000:
    reajuste = 0.04 * salario
    nsalario = salario + reajuste
    print('Novo salario: {:.2f}' .format(nsalario))
    print('Reajuste ganho: {:.2f}' .format(reajuste))
    print('Em percentual: 4 %')
