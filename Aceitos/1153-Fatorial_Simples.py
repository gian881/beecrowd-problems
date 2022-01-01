# https://www.beecrowd.com.br/judge/pt/problems/view/1153

# Ler um valor N. Calcular e escrever seu respectivo fatorial. Fatorial de N = N * (N-1) * (N-2) * (N-3) * ... * 1.

# Entrada
# A entrada contém um valor inteiro N (0 < N < 13).

# Saída
# A saída contém um valor inteiro, correspondente ao fatorial de N.

def main() -> None:

    n = int(input())

    if 0 < n < 13:
        for i in range(n, 1, -1):
            n *= i - 1
        fatorial = n
        print(fatorial)


if __name__ == "__main__":
    main()
