# https://www.urionlinejudge.com.br/judge/pt/problems/view/1145

# Escreva um programa que leia dois valores X e Y. A seguir, mostre uma sequência de 1 até Y, passando para a próxima linha a cada X números.

# Entrada
# O arquivo de entrada contém dois valores inteiros, (1 < X < 20) e (X < Y < 100000).

# Saída
# Cada sequência deve ser impressa em uma linha apenas, com 1 espaço em branco entre cada número, conforme exemplo abaixo. Não deve haver espaço em branco após o último valor da linha.

def main() -> None:

    valores = input().split()
    x, y = [int(num) for num in valores]

    i = 1
    while i <= y:
        if i % x == 0:
            print(f'{i}')
        else:
            print(f'{i} ', end='')
        i += 1


if __name__ == "__main__":
    main()
