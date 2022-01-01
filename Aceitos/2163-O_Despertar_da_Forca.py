# https://www.beecrowd.com.br/judge/pt/problems/view/2163

# Há muito tempo atrás, em uma galáxia muito, muito distante...
# Após o declínio do Império, sucateiros estão espalhados por todo o universo procurando por um sabre de luz perdido. Todos sabem que um sabre de luz emite um padrão de ondas específico: 42 cercado por 7 em toda a volta. Você tem um sensor de ondas que varre um terreno com N x M células. Veja o exemplo abaixo para um terreno 4 x 7 com um sabre de luz nele (na posição (2, 4)).
# https://resources.urionlinejudge.com.br/gallery/images/contests/935.png
# Você deve escrever um programa que, dado um terreno N x M, procura pelo padrão do sabre de luz nele. Nenhuma varredura tem mais do que um padrão de sabre de luz.

# Entrada
# A primeira linha da entrada tem dois números positivos N e M, representando, respectivamente, o número de linhas e de colunas varridos no terreno (3 ≤ N, M ≤ 1000). Cada uma das próximas N linhas tem M inteiros, que descrevem os valores lidos em cada célula do terreno (-100 ≤ Tij ≤ 100, para 1 ≤ i ≤ N e 1 ≤ j ≤ M).

# Saída
# A saída é uma única linha com 2 inteiros X e Y separados por um espaço. Eles representam a coordenada (X,Y) do sabre de luz, caso encontrado. Se o terreno não tem um padrão de sabre de luz, X e Y são ambos zero.

def main() -> None:
    linhas, colunas = [int(numero) for numero in input().split()]
    matriz: list[list[int]] = [
        [int(valor) for valor in input().split()] for _ in range(linhas)]

    for y, linha in enumerate(matriz):
        if y not in {0, linhas-1}:
            for x, celula in enumerate(linha):
                if (x not in {0, colunas - 1} and celula == 42):
                    set_ao_redor: set[int] = {matriz[y - 1][x - 1],
                                              matriz[y - 1][x],
                                              matriz[y - 1][x + 1],
                                              matriz[y][x - 1],
                                              matriz[y][x + 1],
                                              matriz[y + 1][x - 1],
                                              matriz[y + 1][x],
                                              matriz[y + 1][x + 1]}
                    if set_ao_redor == {7}:
                        print(f'{y+1} {x+1}')
                        return
    print('0 0')


if __name__ == "__main__":
    main()
