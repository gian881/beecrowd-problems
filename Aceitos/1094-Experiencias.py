# https://www.beecrowd.com.br/judge/pt/problems/view/1094

# Maria acabou de iniciar seu curso de graduação na faculdade de medicina e precisa de sua ajuda para organizar os experimentos de um laboratório o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

# Entrada
# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

# Saída
# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual deve ser apresentado com dois dígitos após o ponto.

def main() -> None:

    experimentos = int(input())

    cobaias = 0
    sapos = 0
    ratos = 0
    coelhos = 0

    for i in range(0, experimentos):
        valores = input().strip().split()
        quantia = int(valores[0])
        tipo = valores[1]
        if tipo == 'R':
            ratos += quantia
        elif tipo == 'S':
            sapos += quantia
        elif tipo == 'C':
            coelhos += quantia
        cobaias += quantia

    print('Total: {} cobaias' .format(cobaias))
    print('Total de coelhos: {}' .format(coelhos))
    print('Total de ratos: {}' .format(ratos))
    print('Total de sapos: {}' .format(sapos))
    print('Percentual de coelhos: {:.2f} %' .format(100 * coelhos / cobaias))
    print('Percentual de ratos: {:.2f} %' .format(100 * ratos / cobaias))
    print('Percentual de sapos: {:.2f} %' .format(100 * sapos / cobaias))


if __name__ == "__main__":
    main()
