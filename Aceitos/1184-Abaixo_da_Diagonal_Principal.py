# https://www.urionlinejudge.com.br/judge/pt/problems/view/1184

# Leia um caractere maiúsculo, que indica uma operação que deve ser realizada e uma matriz M[12][12]. Em seguida, calcule e
# mostre a soma ou a média considerando somente aqueles elementos que estão abaixo da diagonal principal da matriz, conforme ilustrado abaixo (área verde).
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1184.png

# Entrada
# A primeira linha de entrada contem um único caractere Maiúsculo O  ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

def main() -> None:
    tamanho_da_matriz = 12
    soma: float = 0

    soma_ou_media = input().strip().upper()
    matriz: list[list[float]] = [[float(input()) for _ in range(
        tamanho_da_matriz)] for _ in range(tamanho_da_matriz)]

    for linha_index, linha in enumerate(matriz):
        for coluna_index, celula in enumerate(linha):
            if linha_index > coluna_index:
                soma += celula

    if soma_ou_media == 'S':
        print('{:.1f}' .format(soma))
    else:
        print('{:.1f}' .format(soma / 66))


if __name__ == "__main__":
    main()
