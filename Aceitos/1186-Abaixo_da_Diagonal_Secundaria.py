# https://www.beecrowd.com.br/judge/pt/problems/view/1186

# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e
# mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal Secundária da matriz, conforme ilustrado abaixo (área verde).
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1186.png

# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O  ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

def main() -> None:
    linhas = colunas = 12
    soma: float = 0

    soma_ou_media = input().strip().upper()
    matriz: list[list[float]] = [
        [float(input()) for _ in range(colunas)] for _ in range(linhas)]

    for x in range(1, linhas):
        for y in range(11, 11 - x, -1):
            soma += matriz[x][y]

    if soma_ou_media == 'S':
        print('{:.1f}' .format(soma))
    else:
        print('{:.1f}' .format(soma / 66))


if __name__ == "__main__":
    main()
