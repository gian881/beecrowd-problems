# https://www.beecrowd.com.br/judge/pt/problems/view/1097

# Você deve fazer um programa que apresente a sequencia conforme o exemplo abaixo.

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# Imprima a sequencia conforme exemplo abaixo.

def main() -> None:

    i = 1
    j = 7
    cont = 0

    while cont < 15:
        print('I={} J={}' .format(i, j))
        cont += 1
        if cont % 3 == 0:
            i += 2
            j += 4
        else:
            j -= 1


if __name__ == "__main__":
    main()
