'''

Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

CODIGO      ESPECIFICAÇÃO       PREÇO
1                 Cachorro Quente       R$ 4.0
2                 X - Salada                R$ 4.5
3                 X - Bacon                  R$ 5.0
4                 Torrada Simples        R$ 2.0
5                 Refrigerante             R$ 1.5

Entrada

O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.
Saída

O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.'''
valores = input().strip().split()

codigo = int(valores[0])
quant = int(valores[1])

if codigo == 1:
    valor = 4.0
if codigo == 2:
    valor = 4.5
if codigo == 3:
    valor = 5.0
if codigo == 4:
    valor = 2.0
if codigo == 5:
    valor = 1.5
total = quant * valor
print('Total: R$ {:.2f}' .format(total))
