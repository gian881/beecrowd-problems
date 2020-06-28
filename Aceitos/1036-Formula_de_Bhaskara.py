# Leia 3 valores de ponto flutuante e efetue o cálculo das raízes da equação de Bhaskara. Se não for possível calcular as raízes, mostre a mensagem correspondente “Impossivel calcular”, caso haja uma divisão por 0 ou raiz de numero negativo.

# Entrada
# Leia três valores de ponto flutuante (double) A, B e C.

# Saída
# Se não houver possibilidade de calcular as raízes, apresente a mensagem "Impossivel calcular". Caso contrário, imprima o resultado das raízes com 5 dígitos após o ponto, com uma mensagem correspondente conforme exemplo abaixo. Imprima sempre o final de linha após cada mensagem.
valores = input().strip().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if a == 0:
    print('Impossivel calcular')
else:
    delta = b**2 - 4 * a * c
    if delta < 0:
        print('Impossivel calcular')
    else:
        R1 = (-b + (delta**0.5)) / (2 * a)
        R2 = (-b - (delta**0.5)) / (2 * a)
        print('R1 = {:.5f}' .format(R1))
        print('R2 = {:.5f}' .format(R2))
