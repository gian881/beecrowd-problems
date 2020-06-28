# Faça um programa que leia um vetor X[10]. Substitua a seguir, todos os valores nulos e negativos do vetor X por 1. Em seguida mostre o vetor X.

# Entrada
# A entrada contém 10 valores inteiros, podendo ser positivos ou negativos.

# Saída
# Para cada posição do vetor, escreva "X[i] = x", onde i é a posição do vetor e x é o valor armazenado naquela posição.

x = [None] * 10

for i in range(10):
    a = int(input())
    x[i] = a
for c, d in enumerate(x):
    # c = indice
    # d = numero
    if d <= 0:
        print('X[{}] = 1' .format(c))
    else:
        print('X[{}] = {}' .format(c, d))
