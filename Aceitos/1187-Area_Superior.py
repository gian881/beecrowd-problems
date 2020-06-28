# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média considerando somente aqueles elementos que estão na área superior da matriz, conforme ilustrado abaixo (área verde).
# https://urionlinejudge.r.worldssl.net/gallery/images/problems/UOJ_1187.png

# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem 144 valores com ponto flutuante de dupla precisão que compõem a matriz.

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

for x in range(5):
    for y in range(x + 1, 11 - x):
        soma += matriz[x][y]

if r == 'S':
    print('{:.1f}' .format(soma))
else:
    print('{:.1f}' .format(soma / 30))
