# https://www.beecrowd.com.br/judge/pt/problems/view/2552

# Está chegando a grande final do Campeonato Nlogonense de Surf Aquático, que este ano ocorrerá na cidade de Bonita Horeleninha (BH)! Nesta cidade, o jogo PãodeQueijoSweeper é bastante popular!
# O tabuleiro do jogo consiste em uma matriz de N linhas e M colunas. Cada célula da matriz contém um pão de queijo ou o número de pães de queijo que existem nas celulas adjacentes a ela. Uma célula é adjacente a outra se estiver imediatamente à esquerda, à direita, acima ou abaixo da célula. Note que, se não contiver um pão de queijo, uma célula deve obrigatoriamente conter um número entre 0 e 4, inclusive.
# Dadas as posições dos pães de queijo, determine o tabuleiro do jogo!

# Entrada
# A entrada contém vários casos de teste. A primeira linha de cada caso contém os inteiros N e M (1 ≤ N, M ≤ 100). As próximas N linhas contém M inteiros cada, separados por espaços, descrevendo os pães de queijo no tabuleiro. O j-ésimo inteiro da i-ésima linha é 1 se existe um pão de queijo na linha i e coluna j do tabuleiro, ou 0 caso contrário.
# A entrada termina com fim-de-arquivo (EOF).

# Saída
# Para cada caso de teste, imprima N linhas com M inteiros cada, não separados por espaços, descrevendo a configuração do tabuleiro. Se uma posição contém um pão de queijo, imprima 9 para ela; caso contrário, imprima o número cuja posição deve conter.

def contar_paes(tabuleiro, linha, coluna):
    contador = 0

    if linha != 0 and tabuleiro[linha - 1][coluna] == 1:
        contador += 1

    if linha != len(tabuleiro) - 1 and tabuleiro[linha + 1][coluna] == 1:
        contador += 1

    if coluna != 0 and tabuleiro[linha][coluna-1] == 1:
        contador += 1

    if coluna != len(tabuleiro[linha]) - 1 and tabuleiro[linha][coluna+1] == 1:
        contador += 1

    return contador


def main() -> None:
    while True:
        try:
            linhas, colunas = map(int, input().split())
            tabuleiro: list[list[int]] = [list(map(int, input().split()))
                                          for _ in range(linhas)]
            tabuleiro_final: list[list[int]] = [
                [0 for _ in range(colunas)] for _ in range(linhas)]
            for i in range(linhas):
                for j in range(colunas):
                    tabuleiro_final[i][j] = 9 if tabuleiro[i][j] == 1 else contar_paes(
                        tabuleiro, i, j)
            for linha in tabuleiro_final:
                for numero in linha:
                    print(numero, end='')
                print()

        except EOFError:
            break


if __name__ == "__main__":
    main()
