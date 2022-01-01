# https://www.beecrowd.com.br/judge/pt/problems/view/1151

# A seguinte sequência de números 0 1 1 2 3 5 8 13 21... é conhecida como série de Fibonacci. Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 46).

# Saída
# Os valores devem ser mostrados na mesma linha, separados por um espaço em branco. Não deve haver espaço após o último valor.

def main() -> None:
    t = int(input())
    a = 0
    b = 1
    print('{} {} ' .format(a, b), end='')
    counter = 3
    while counter <= t:
        c = a + b
        if counter < t:
            print('{} ' .format(c), end='')
        else:
            print('{}' .format(c))
        a = b
        b = c
        counter += 1


if __name__ == "__main__":
    main()
