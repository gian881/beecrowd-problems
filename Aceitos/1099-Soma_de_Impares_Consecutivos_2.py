# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de todos os ímpares existentes entre X e Y.

# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

# Saída
# Imprima a soma de todos valores ímpares entre X e Y.

n = int(input())

for i in range(n):
    valores = input().strip().split()

    x = int(valores[0])
    y = int(valores[1])

    lista = [x, y]
    lista = sorted(lista)

    x = lista[0]
    y = lista[1]

    soma = 0

    for i in range(x + 1, y):
        if i % 2 != 0:
            soma += i

    print(soma)
