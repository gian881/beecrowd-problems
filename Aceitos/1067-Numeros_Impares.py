# https://www.urionlinejudge.com.br/judge/pt/problems/view/1067

# Leia um valor inteiro X (1 <= X <= 1000). Em seguida mostre os ímpares de 1 até X, um valor por linha, inclusive o X, se for o caso.

# Entrada
# O arquivo de entrada contém 1 valor inteiro qualquer.

# Saída
# Imprima todos os valores ímpares de 1 até X, inclusive X, se for o caso.

def main() -> None:
    x = int(input())
    for i in range(1, x + 1):
        if i % 2 != 0:
            print(i)


if __name__ == "__main__":
    main()
