# https://www.beecrowd.com.br/judge/pt/problems/view/2310

# Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques do time todo tiveram sucesso.

# Entrada
# A entrada é dada pelo número de jogadores N (1 ≤ N ≤ 100), seguido pelo nome de cada um dos jogadores. Abaixo do nome de cada jogador, seguem duas linhas com três inteiros cada. Na primeira linha S, B e A (0 ≤ S,B,A ≤ 10000) representam a quantidade de tentativas de saques, bloqueios e ataques e na segunda linha, S1, B1 e A1 (0 ≤ S1 ≤ S; 0 ≤ B1 ≤ B; 0 ≤ A1 ≤ A) com o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

# Saída
# A saída deve conter o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme mostrado no exemplo.

def main() -> None:
    total_saques: int = 0
    total_bloqueios: int = 0
    total_ataques: int = 0
    total_saques_s: int = 0
    total_bloqueios_s: int = 0
    total_ataques_s: int = 0

    for _ in range(int(input())):
        input()
        saques, bloqueios, ataques = [int(x) for x in input().split()]
        total_saques += saques
        total_bloqueios += bloqueios
        total_ataques += ataques
        saques_s, bloqueios_s, ataques_s = [int(x) for x in input().split()]
        total_saques_s += saques_s
        total_bloqueios_s += bloqueios_s
        total_ataques_s += ataques_s

    print(f'Pontos de Saque: {(total_saques_s / total_saques) * 100:.2f} %.')
    print(
        f'Pontos de Bloqueio: {(total_bloqueios_s / total_bloqueios) * 100:.2f} %.')
    print(
        f'Pontos de Ataque: {(total_ataques_s / total_ataques) * 100:.2f} %.')


if __name__ == "__main__":
    main()
