# https://www.beecrowd.com.br/judge/pt/problems/view/1075

# Leia um valor inteiro N. Apresente todos os números entre 1 e 10000 que divididos por N dão resto igual a 2.

# Entrada
# A entrada contém um valor inteiro N (N < 10000).

# Saída
# Imprima todos valores que quando divididos por N dão resto = 2, um por linha.

def main() -> None:

    n = int(input())
    for i in range(1, 10001):
        if i % n == 2:
            print(i)


if __name__ == "__main__":
    main()
