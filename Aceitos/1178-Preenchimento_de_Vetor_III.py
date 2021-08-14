# https://www.urionlinejudge.com.br/judge/pt/problems/view/1178

# Leia um valor X. Coloque este valor na primeira posição de um vetor N[100].
# Em cada posição subsequente de N (1 até 99), coloque a metade do valor
# armazenado na posição anterior, conforme o exemplo abaixo.
# Imprima o vetor  N.

# Entrada
# A entrada contem um valor de dupla precisão com 4 casas decimais.

# Saída
# Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor
# armazenado naquela posição. Cada valor do vetor deve ser apresentado com 4 casas decimais.

def main() -> None:
    numero = float(input())
    lista = [numero]
    for i in range(1, 100):
        lista.append(lista[i - 1] / 2)

    for index, valor in enumerate(lista):
        print(f'N[{index}] = {valor:.4f}')


if __name__ == "__main__":
    main()
