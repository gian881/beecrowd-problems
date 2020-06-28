'''Leia 3 valores de ponto flutuante A, B e C e ordene-os em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o tipo de triângulo que estes três lados formam, com base nos seguintes casos, sempre escrevendo uma mensagem adequada:
    se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
    se A2 = B2 + C2, apresente a mensagem: TRIANGULO RETANGULO
    se A2 > B2 + C2, apresente a mensagem: TRIANGULO OBTUSANGULO
    se A2 < B2 + C2, apresente a mensagem: TRIANGULO ACUTANGULO
    se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
    se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES

Entrada
A entrada contem três valores de ponto flutuante de dupla precisão A (0 < A) , B (0 < B) e C (0 < C).

Saída
Imprima todas as classificações do triângulo especificado na entrada.'''

valores = input().strip().split()

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

lista = [A, B, C]
lista = sorted(lista, reverse=True)
a = lista[0]
b = lista[1]
c = lista[2]

if a < b + c and b < a + c and c < a + b:
    if a * a == b * b + c * c:
        print('TRIANGULO RETANGULO')
    if a * a > b * b + c * c:
        print('TRIANGULO OBTUSANGULO')
    if a * a < b * b + c * c:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    if a == b and a != c and b != c or a == c and a != b and c != b or b == c and b != a and c != a:
        print('TRIANGULO ISOSCELES')
else:
    print('NAO FORMA TRIANGULO')
