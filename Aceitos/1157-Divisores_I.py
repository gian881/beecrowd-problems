# https://www.urionlinejudge.com.br/judge/pt/problems/view/1157

# Ler um número inteiro N e calcular todos os seus divisores.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Escreva todos os divisores positivos de N, um valor por linha.

def main() -> None:

    n = int(input())

    for i in range(1, n + 1):
        if n % i == 0:
            print(i)


if __name__ == "__main__":
    main()
