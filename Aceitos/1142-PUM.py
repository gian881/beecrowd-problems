# https://www.urionlinejudge.com.br/judge/pt/problems/view/1142

# Escreva um programa que leia um valor inteiro N. Este N é a quantidade
# de linhas de saída que serão apresentadas na execução do programa.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N.

# Saída
# Imprima a saída conforme o exemplo fornecido.

def main() -> None:

    x = 1
    y = 2
    z = 3
    n = int(input())

    for i in range(n):
        print('{} {} {} PUM' .format(x, y, z))
        x += 4
        y += 4
        z += 4


if __name__ == "__main__":
    main()
