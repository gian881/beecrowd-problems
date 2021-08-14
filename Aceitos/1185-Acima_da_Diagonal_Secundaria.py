# https://www.urionlinejudge.com.br/judge/pt/problems/view/1185

# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e
# mostre a soma ou a média considerando somente aqueles elementos que estão acima da diagonal secundária da matriz, conforme ilustrado abaixo (área verde).
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1185.png

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

    for x in range(linhas - 1):
        for y in range(colunas - 1 - x):
            soma += matriz[x][y]

    if soma_ou_media == 'S':
        print('{:.1f}' .format(soma))
    else:
        print('{:.1f}' .format(soma / 66))


if __name__ == "__main__":
    main()
