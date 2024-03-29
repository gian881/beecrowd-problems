# https://www.beecrowd.com.br/judge/pt/problems/view/2139

# Pedrinho é um garoto que adora festas em família, principalmente o Natal, quando ganha presente dos pais e dos avós. Esse ano, seu pai lhe prometeu um PS4, mas somente se Pedrinho conseguir resolver alguns desafios ao longo do ano, sendo um deles, escrever um programa que calcule quantos dias faltam para o Natal.
# Entretanto, Pedrinho tem somente 9 anos e não tem noção alguma de programação, mas sabe que você, primo dele, mexe com "coisas de computador", e dessa forma, pediu para você escrever o programa para ele. Não somente isso, mas prometeu que deixaria você jogar todo final de semana e por quanto tempo quiser!

# Entrada
# A entrada é composta por vários casos de teste. Cada linha contém o mês e o dia do ano de 2016 (ano bissexto). A entrada termina com fim de arquivo.

# Saída
# Se for Natal, imprima "E natal!"; se faltar somente um dia, imprima "E vespera de natal!"; se já passou, imprima "Ja passou!". Caso contrário, imprima "Faltam X dias para o natal!", sendo X o número de dias que faltam para o Natal.
from datetime import date, timedelta


def main() -> None:
    natal: date = date(2016, 12, 25)
    while True:
        try:
            mes, dia = [int(x) for x in input().split()]
            data = date(2016, mes, dia)
            if data == natal:
                print('E natal!')
            elif data + timedelta(days=1) == natal:
                print('E vespera de natal!')
            elif data > natal:
                print('Ja passou!')
            else:
                print(f'Faltam {(natal - data).days} dias para o natal!')
        except EOFError:
            break


if __name__ == "__main__":
    main()
