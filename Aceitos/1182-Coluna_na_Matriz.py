# https://www.urionlinejudge.com.br/judge/pt/problems/view/1182

# Neste problema você deve ler um número que indica uma coluna de uma matriz na qual uma operação deve ser realizada, um caractere maiúsculo, indicando a operação que será realizada, e
# todos os elementos de uma matriz M[12][12]. Em seguida, calcule e mostre a soma ou a média dos elementos que estão na área verde da matriz,
# conforme for o caso. A imagem abaixo ilustra o caso da entrada do valor 5 para a coluna da matriz, demonstrando os elementos que deverão ser
# considerados na operação.
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1182.png

# Entrada
# A primeira linha de entrada contem um número C (0 ≤ C ≤ 11) indicando a coluna que será considerada para operação.
# A segunda linha de entrada contém um único caractere Maiúsculo T ('S' ou 'M'), indicando a operação
# (Soma ou Média) que deverá ser realizada com os elementos da matriz. Seguem os 144 valores de ponto flutuante que compõem a matriz.

# Saída
# Imprima o resultado solicitado (a soma ou média), com 1 casa após o ponto decimal.

def main() -> None:
    tamanho_da_matriz = 12
    soma: float = 0

    coluna = int(input())
    soma_ou_media = input().upper().strip()
    matriz: list[list[float]] = [[float(input())
                                  for _ in range(tamanho_da_matriz)] for _ in range(tamanho_da_matriz)]

    for linha in matriz:
        soma += linha[coluna]

    if soma_ou_media == 'S':
        print('{:.1f}' .format(soma))
    else:
        print('{:.1f}' .format(soma / tamanho_da_matriz))


if __name__ == "__main__":
    main()
