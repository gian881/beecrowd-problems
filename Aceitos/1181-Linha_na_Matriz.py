# https://www.urionlinejudge.com.br/judge/pt/problems/view/1181

# Neste problema você deve ler um número, indicando uma linha da matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e
# todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz,
# conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 2 para a linha da matriz, demonstrando os elementos que deverão ser
# considerados na operação.
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1181.png

# Entrada
# A primeira linha de entrada contem um número L (0 ≤ L ≤ 11) indicando a linha que será considerada para operação. A segunda linha de entrada contém um
# único caractere Maiúsculo T ('S' ou 'M'), indicando a operação (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz, sendo que a mesma é preenchida linha por linha, da linha 0 até a linha 11, sempre da esquerda para a direita.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

def main() -> None:
    tamanho_da_matriz = 12
    soma: float = 0

    line = int(input())
    op = input().upper().strip()  # SOMA OU MEDIA
    matriz: list[list[float]] = [[float(input()) for _ in range(
        tamanho_da_matriz)] for _ in range(tamanho_da_matriz)]

    for celula in matriz[line]:
        soma += celula

    if op == 'S':
        print('{:.1f}' .format(soma))
    else:
        print('{:.1f}' .format(soma / tamanho_da_matriz))


if __name__ == "__main__":
    main()
