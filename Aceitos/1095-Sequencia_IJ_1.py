# https://www.beecrowd.com.br/judge/pt/problems/view/1095

# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo

def main() -> None:

    j = 60
    i = 1

    while j > -1:
        print('I={} J={}' .format(i, j))
        i += 3
        j -= 5


if __name__ == "__main__":
    main()
