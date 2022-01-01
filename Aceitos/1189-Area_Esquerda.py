# https://www.beecrowd.com.br/judge/pt/problems/view/1189

# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e
# mostre a soma ou a média considerando somente aqueles elementos que estão na área esquerda da matriz, conforme ilustrado abaixo (área verde).
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1189.png

# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O  ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

def main() -> None:

    linhas = colunas = 12
    matriz = []
    soma: float = 0

    r = input().strip().upper()

    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            valor = float(input())
            linha.append(valor)
        matriz.append(linha)

    for x in range(1, linhas - 1):
        if x <= 5:
            for y in range(x):
                soma += matriz[x][y]
        else:
            for y in range(colunas - 1 - x):
                soma += matriz[x][y]

    if r == 'S':
        print('{:.1f}' .format(soma))
    else:
        print('{:.1f}' .format(soma / 30))


if __name__ == "__main__":
    main()
