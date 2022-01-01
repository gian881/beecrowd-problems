# https://www.beecrowd.com.br/judge/pt/problems/view/1187

# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e
# mostre a soma ou a média considerando somente aqueles elementos que estão na área superior da matriz, conforme ilustrado abaixo (área verde).
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1187.png

# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O  ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem 144 valores com ponto flutuante de dupla precisão que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

def main() -> None:

    linhas: int = 12
    colunas: int = 12
    matriz: list[list[float]] = [[] for _ in range(linhas)]
    soma: float = 0

    r = input().strip().upper()

    for linha in matriz:
        for _ in range(colunas):
            linha.append(float(input()))

    for x in range(5):
        for y in range(x + 1, 11 - x):
            soma += matriz[x][y]

    if r == 'S':
        print(f'{soma:.1f}')
    else:
        print(f'{soma/30:.1f}')

    if __name__ == "__main__":
        main()


if __name__ == "__main__":
    main()
