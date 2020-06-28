# No oitavo episodio da segunda temporada do seriado The Big Bang Theory, The Lizard-Spock Expansion, Sheldon e Raj discutem qual dos dois é o melhor: o filme Saturn 3 ou a série Deep Space 9. A sugestão de Raj para a resolução do impasse é uma disputa de Pedra-Papel-Tesoura. Contudo, Sheldon argumenta que, se as partes envolvidas se conhecem, entre 75% e 80% das disputas de Pedra-Papel-Tesoura terminam empatadas, e então sugere o Pedra-Papel-Tesoura-Lagarto-Spock.
# As regras do jogo proposto são:

#     a tesoura corta o papel;
#     o papel embrulha a pedra;
#     a pedra esmaga o lagarto;
#     o lagarto envenena Spock;
#     Spock destrói a tesoura;
#     a tesoura decapita o lagarto;
#     o lagarto come o papel;
#     o papel contesta Spock;
#     Spock vaporiza a pedra;
#     a pedra quebra a tesoura.

# Embora a situação não se resolva no episódio (ambos escolhem Spock, resultando em um empate), não é difıcil deduzir o que aconteceria se a disputa continuasse. Caso Sheldon vencesse, ele se deleitaria com a vitória, exclamando "Bazinga!"; caso Raj vencesse, ele concluiria que "Raj trapaceou!"; caso o resultado fosse empate, ele exigiria nova partida: "De novo!". Conhecidas as personagens do jogo escolhido por ambos, faça um programa que imprima a provável reação de Sheldon.

# Entrada
# A entrada consiste em uma série de casos de teste. A primeira linha contém um inteiro positivo T (T ≤ 100), que representa o número de casos de teste. Cada caso de teste é representado por uma linha da entrada, contendo as escolhas de Sheldon e Raj, respectivamente, separadas por um espaço em branco. As escolha possíveis são as personagens do jogo: pedra, papel, tesoura, lagarto e Spock.

# Saida
# Para cada caso de teste deverá ser impressa a mensagem "Caso #t: R", onde t é o número do caso de teste (cuja contagem se inicia no número um) e R é uma das três reações possíveis de Sheldon: "Bazinga!", "Raj trapaceou!", ou "De novo!".
casos = int(input())


def win(a, b):
    if a == 'tesoura' and b == 'papel':
        return 1
    elif a == 'papel' and b == 'tesoura':
        return 2
    elif a == 'papel' and b == 'pedra':
        return 1
    elif a == 'pedra' and b == 'papel':
        return 2
    elif a == 'pedra' and b == 'lagarto':
        return 1
    elif a == 'lagarto' and b == 'pedra':
        return 2
    elif a == 'lagarto' and b == 'Spock':
        return 1
    elif a == 'Spock' and b == 'lagarto':
        return 2
    elif a == 'Spock' and b == 'tesoura':
        return 1
    elif a == 'tesoura' and b == 'Spock':
        return 2
    elif a == 'tesoura' and b == 'lagarto':
        return 1
    elif a == 'lagarto' and b == 'tesoura':
        return 2
    elif a == 'lagarto' and b == 'papel':
        return 1
    elif a == 'papel' and b == 'lagarto':
        return 2
    elif a == 'papel' and b == 'Spock':
        return 1
    elif a == 'Spock' and b == 'papel':
        return 2
    elif a == 'Spock' and b == 'pedra':
        return 1
    elif a == 'pedra' and b == 'Spock':
        return 2
    elif a == 'pedra' and b == 'tesoura':
        return 1
    elif a == 'tesoura' and b == 'pedra':
        return 2
    else:
        return 3


for i in range(1, casos + 1):
    pptls = input().strip().split()
    sheldon, raj = pptls[0], pptls[1]

    reacao = win(sheldon, raj)
    if reacao == 1:
        reacao = 'Bazinga!'
    elif reacao == 2:
        reacao = 'Raj trapaceou!'
    elif reacao == 3:
        reacao = 'De novo!'

    print('Caso #{}: {}'.format(i, reacao))
