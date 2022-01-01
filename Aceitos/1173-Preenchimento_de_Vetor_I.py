# https://www.beecrowd.com.br/judge/pt/problems/view/1173

# Leia um valor e faça um programa que coloque o valor lido na primeira posição de um vetor N[10]. Em cada posição subsequente, coloque o dobro do valor da posição anterior. Por exemplo, se o valor lido for 1, os valores do vetor devem ser 1,2,4,8 e assim sucessivamente. Mostre o vetor em seguida.

# Entrada
# A entrada contém um valor inteiro (V<=50).

# Saída
# Para cada posição do vetor, escreva "N[i] = X", onde i é a posição do vetor e X é o valor armazenado na posição i. O primeiro número do vetor N (N[0]) irá receber o valor de V.

def main() -> None:
    numero_inicial = int(input())
    lista: list[int] = [numero_inicial] + [0 for _ in range(9)]

    for i in range(1, 10):
        lista[i] = lista[(i - 1)] * 2

    for indice, valor in enumerate(lista):
        print(f'N[{indice}] = {valor}' .format(indice, valor))


if __name__ == "__main__":
    main()
