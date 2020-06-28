# Faça um programa que leia um valor e apresente o número de Fibonacci correspondente a este valor lido. Lembre que os 2 primeiros elementos da série de Fibonacci são 0 e 1 e cada próximo termo é a soma dos 2 anteriores a ele. Todos os valores de Fibonacci calculados neste problema devem caber em um inteiro de 64 bits sem sinal.

# Entrada
# A primeira linha da entrada contém um inteiro T, indicando o número de casos de teste. Cada caso de teste contém um único inteiro N (0 ≤ N ≤ 60), correspondente ao N-esimo termo da série de Fibonacci.

# Saída
# Para cada caso de teste da entrada, imprima a mensagem "Fib(N) = X", onde X é o N-ésimo termo da série de Fibonacci.

t = 61
fibonacci = [None] * t
a, b = 0, 1
fibonacci[0], fibonacci[1] = a, b
for i in range(2, t):
    c = a + b
    fibonacci[i] = c
    a = b
    b = c

testes = int(input())

for i in range(testes):
    index = int(input())
    print('Fib({}) = {}' .format(index, fibonacci[index]))
