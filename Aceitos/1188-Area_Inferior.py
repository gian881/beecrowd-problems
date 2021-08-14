# https://www.urionlinejudge.com.br/judge/pt/problems/view/1188

# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e
# mostre a soma ou a média considerando somente aqueles elementos que estão na área inferior da matriz, conforme ilustrado abaixo (área verde).
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1188.png

# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O  ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante de dupla precisão (double) que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

def main() -> None:

    linhas = colunas = 12
    matriz: list[list[float]] = []
    soma: float = 0
    r = input().strip().upper()
    for _ in range(linhas):
        linha = []
        for _ in range(colunas):
            valor = float(input())
            linha.append(valor)
        matriz.append(linha)
    for x in range(7, linhas):
        for y in range(colunas - x, x):
            soma += matriz[x][y]
    if r == 'S':
        print('{:.1f}' .format(soma))
    else:
        print('{:.1f}' .format(soma / 30))


if __name__ == "__main__":
    main()
