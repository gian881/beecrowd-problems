# https://www.urionlinejudge.com.br/judge/pt/problems/view/2221

# Depois de capturar muitos Pomekons, Dabriel e Guarte resolveram batalhar. A forma de duelo é simples, cada treinador coloca um Pomekon na batalha e vence quem tem o Pomekon com maior valor de golpe, que é definido da seguinte maneira:
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_2221.png
# O Bônus será dado ao Pomekon do treinador que estiver em um level de valor par.
# Neste problema será dado a você o valor do bônus aplicado, os valores de ataque e defesa do Pomekon de Dabriel e Guarte e seus respectivos níveis, cabe a você informar o ganhador da batalha.

# Entrada
# A entrada é composta por
# diversas instâncias. A primeira linha da entrada contém um inteiro T
# indicando o número de instâncias.

# Cada instância começa com um inteiro B (0 ≤
# B ≤ 100), que indica o valor do bônus aplicado. Nas
# duas linhas seguintes terão três inteiros Ai,
# Di e Li (1 ≤ Ai,
# Di ≤ 100, 1 ≤ Li ≤ 50),
# representado o valor de ataque do Pomekon, o valor de defesa e o
# level do treinador. A primeira linha representa o Pomekon de Dabriel
# e a segunda o de Guarte.

# Saída
# Para instância na entrada você deverá imprimir o nome do treinador que irá vencer a batalha, em caso de empate imprima: "Empate", sem aspas.

def calcular_valor_golpe(ataque: int, defesa: int, level: int, bonus: int = 0) -> float:
    return((ataque + defesa)/2) + (bonus if level % 2 == 0 else 0)


def main() -> None:
    casos = int(input())

    for _ in range(casos):
        bonus = int(input())
        ataque_d, defesa_d, level_d = [int(x) for x in input().split()]
        ataque_g, defesa_g, level_g = [int(x) for x in input().split()]

        golpe_d = calcular_valor_golpe(ataque_d, defesa_d, level_d, bonus)
        golpe_g = calcular_valor_golpe(ataque_g, defesa_g, level_g, bonus)

        if golpe_d == golpe_g:
            print("Empate")
        elif golpe_d > golpe_g:
            print("Dabriel")
        else:
            print("Guarte")


if __name__ == "__main__":
    main()
