# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

valores = input().strip().split()

a = int(valores[0])
b = int(valores[1])
c = int(valores[2])

maior = a
if b > maior:
    maior = b
elif c > maior:
    maior = c
print('{} eh o maior' .format(maior))
