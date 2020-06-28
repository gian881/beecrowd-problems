# Leia 5 valores Inteiros. A seguir mostre quantos valores digitados foram pares, quantos valores digitados foram ímpares, quantos valores digitados foram positivos e quantos valores digitados foram negativos.
#
# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.
#
# Saída
# Imprima a mensagem conforme o exemplo fornecido, uma mensagem por linha, não esquecendo o final de linha após cada uma.
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(0, 5):
    valor = int(input())
    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1
    if valor > 0:
        positivos += 1
    elif valor < 0:
        negativos += 1
print('{} valor(es) par(es)' .format(pares))
print('{} valor(es) impar(es)' .format(impares))
print('{} valor(es) positivo(s)' .format(positivos))
print('{} valor(es) negativo(s)' .format(negativos))
