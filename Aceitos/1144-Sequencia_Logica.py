# Escreva um programa que leia um valor inteiro N. N * 2 linhas de saída serão apresentadas na execução do programa, seguindo a lógica do exemplo abaixo. Para valores com mais de 6 dígitos, todos os dígitos devem ser apresentados.

# Entrada
# O arquivo de entrada contém um número inteiro positivo N (1 < N < 1000).

# Saída
# Imprima a saída conforme o exemplo fornecido.

n = int(input())
n *= 2
x = y = z = 1

# x = 1 a cada impar
# y = +1 no par e +i -1 no impar
# z = x * y no impar z = z+1 no par

for i in range(1, n + 1):
    if i % 2 == 1 and i != 1:
        y += i - 1
        x += 1
        z = x * y

    if i % 2 == 0:
        y += 1
        z += 1

    print(x, y, z)

# COMPLEXO PRA CARALHO MSM
