# https://www.urionlinejudge.com.br/judge/pt/problems/view/1143

# Escreva um programa que leia um valor inteiro N (1 < N < 1000). Este N é a quantidade de linhas de saída que serão apresentadas na execução do programa.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N.

# Saída
# Imprima a saída conforme o exemplo fornecido.

def main() -> None:

    n = int(input())
    x = 1

    for i in range(n):
        print('{} {} {}' .format(x, x**2, x**3))
        x += 1


if __name__ == "__main__":
    main()
