# https://www.beecrowd.com.br/judge/pt/problems/view/1959

# Na geometria Euclidiana, um polígono regular é um polígono em que todos os ângulos são iguais e todos os lados tem o mesmo comprimento. Um polígono simples é aquele cujos segmentos de reta não se interceptam. Abaixo pode-se ver vários mosaicos feitos por polígonos regulares.
# https://www.urionlinejudge.com.br/gallery/images/contests/C_1.jpg
# Você deve escrever um programa que, dados o número e o comprimento dos lados de um polígono regular, mostre seu perímetro.

# Entrada
# A entrada tem dois inteiros positivos: N e L, que são, respectivamente, o número de lados e o comprimento de cada lado de um polígono regular (3 ≤ N ≤ 1000000 and 1 ≤ L ≤ 4000).

# Saída
# A saída é o perímetro P do polígono regular em uma única linha.

def main() -> None:
    n, l = [int(x) for x in input().split()]
    print(n*l)


if __name__ == "__main__":
    main()
