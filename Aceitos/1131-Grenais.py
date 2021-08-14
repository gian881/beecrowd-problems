# https://www.urionlinejudge.com.br/judge/pt/problems/view/1131

# A Federação Gaúcha de Futebol contratou você para escrever um programa para fazer uma estatística do resultado de vários GRENAIS. Escreva um programa para ler o número de gols marcados pelo Inter e pelo Grêmio em um GRENAL. Logo após escrever a mensagem "Novo grenal (1-sim 2-nao)" e solicitar uma resposta. Se a resposta for 1, o algoritmo deve ser executado novamente solicitando o número de gols marcados pelos times em uma nova partida, caso contrário deve ser encerrado imprimindo:
# - Quantos GRENAIS fizeram parte da estatística.
# - O número de vitórias do Inter.
# - O número de vitórias do Grêmio.
# - O número de Empates.
# - Uma mensagem indicando qual o time que venceu o maior número de GRENAIS (ou "Nao houve vencedor", caso termine empatado).

# Entrada
# O arquivo de entrada contém 2 valores inteiros, correspondentes aos gols marcados pelo Inter e pelo Grêmio respectivamente. Em seguida háverá um inteiro (1 ou 2), correspondente à repetição do programa.

# Saída
# Após cada leitura dos gols, deve ser impressa a mensagem "Novo grenal (1-sim 2-nao)". Quando o algoritmo for encerrado devem ser mostradas as estatísticas conforme a descrição apresentada acima. Obs: a palavra "Gremio" deve ser impressa sem acento, conforme o exemplo abaixo.

def main() -> None:

    interwins = 0
    gremiowins = 0
    empates = 0
    grenais = 1

    while True:
        gols = input().strip().split()

        inter = int(gols[0])
        gremio = int(gols[1])

        if inter > gremio:
            interwins += 1
        if gremio > inter:
            gremiowins += 1
        if gremio == inter:
            empates += 1

        resposta = 0
        while resposta != 1 and resposta != 2:
            print('Novo grenal (1-sim 2-nao)')
            resposta = int(input())
        if resposta == 2:
            break

        grenais += 1
        inter = gremio = 0
    print('{} grenais' .format(grenais))
    print('Inter:{}' .format(interwins))
    print('Gremio:{}' .format(gremiowins))
    print('Empates:{}' .format(empates))
    if gremiowins > interwins:
        print('Gremio venceu mais')
    elif interwins > gremiowins:
        print('Inter venceu mais')
    else:
        print('Nao houve vencedor')


if __name__ == "__main__":
    main()
