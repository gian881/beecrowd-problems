# https://www.beecrowd.com.br/judge/pt/problems/view/1079

# Leia 1 valor inteiro N, que representa o número de casos de teste que
# vem a seguir. Cada caso de teste consiste de 3 valores reais, cada um
# deles com uma casa decimal. Apresente a média ponderada para cada um
# destes conjuntos de 3 valores, sendo que o primeiro valor tem peso 2, o
# segundo valor tem peso 3 e o terceiro valor tem peso 5.

# Entrada
# O arquivo de entrada contém um valor inteiro N na primeira linha. Cada N linha a seguir contém um caso de teste com três valores com uma casa decimal cada valor.

# Saída
# Para cada caso de teste, imprima a média ponderada dos 3 valores, conforme exemplo abaixo.

def main() -> None:

    n = int(input())

    for i in range(0, n):
        valores = input().strip().split()
        a = float(valores[0])
        b = float(valores[1])
        c = float(valores[2])
        media = ((a * 2) + (b * 3) + (c * 5)) / 10
        print('{:.1f}' .format(media))


if __name__ == "__main__":
    main()
