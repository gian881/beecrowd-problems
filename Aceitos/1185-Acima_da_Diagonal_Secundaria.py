# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal secundária da matriz, conforme ilustrado abaixo (área verde).
# https://urionlinejudge.r.worldssl.net/gallery/images/problems/UOJ_1185.pnghttps://urionlinejudge.r.worldssl.net/gallery/images/problems/UOJ_1185.png

# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

linhas = colunas = 12
matriz = []
soma = 0

r = input().strip().upper()

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = float(input())
        linha.append(valor)
    matriz.append(linha)

for x in range(linhas - 1):
    for y in range(colunas - 1 - x):
        soma += matriz[x][y]
        # print(M[x][y])

if r == 'S':
    print('{:.1f}' .format(soma))
else:
    print('{:.1f}' .format(soma / 66))
