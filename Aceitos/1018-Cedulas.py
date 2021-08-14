# https://www.urionlinejudge.com.br/judge/pt/problems/view/1018

# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Saída
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.

def main() -> None:
    valor = int(input())
    print(valor)

    notas = valor // 100
    valor %= 100
    print('{} nota(s) de R$ 100,00' .format(notas))

    notas = valor // 50
    valor %= 50
    print('{} nota(s) de R$ 50,00' .format(notas))

    notas = valor // 20
    valor %= 20
    print('{} nota(s) de R$ 20,00' .format(notas))

    notas = valor // 10
    valor %= 10
    print('{} nota(s) de R$ 10,00' .format(notas))

    notas = valor // 5
    valor %= 5
    print('{} nota(s) de R$ 5,00' .format(notas))

    notas = valor // 2
    valor %= 2
    print('{} nota(s) de R$ 2,00' .format(notas))

    notas = valor // 1
    valor %= 1
    print('{} nota(s) de R$ 1,00' .format(notas))


if __name__ == "__main__":
    main()
