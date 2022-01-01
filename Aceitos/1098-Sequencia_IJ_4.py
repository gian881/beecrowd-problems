# https://www.beecrowd.com.br/judge/pt/problems/view/1098

# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo.

from decimal import Decimal


def number(numero: Decimal) -> Decimal:
    num_str_list: list[str] = str(numero).split('.')
    if len(num_str_list) > 1:
        return Decimal(num_str_list[0]) if num_str_list[1] == '0' else numero
    else:
        return numero


def main() -> None:

    i: Decimal = Decimal(0)
    j: Decimal = Decimal(1)

    for cont in range(1, 34):
        i, j = number(i), number(j)
        print(f'I={i} J={j}')
        if cont % 3 == 0:
            i += Decimal('0.2')
            j -= 2
            j += Decimal('0.2')
        else:
            j += 1


if __name__ == "__main__":
    main()
