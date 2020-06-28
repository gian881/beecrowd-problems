# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

# Entrada
# O arquivo de entrada contém 100 números inteiros, positivos e distintos.

# Saída
# Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

lista = []
maior = 0

for i in range(0, 100):
    a = int(input())
    if a > maior:
        maior = a
    lista.append(a)

print(maior)
print(lista.index(maior) + 1)
