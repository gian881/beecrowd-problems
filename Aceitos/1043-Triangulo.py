# Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
# Perimetro = XX.X
# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem
# Area = XX.X
#
# Entrada
# A entrada contém três valores reais.
#
# Saída
# O resultado deve ser apresentado com uma casa decimal.

valores = input().strip().split()

a = float(valores[0])
b = float(valores[1])
c = float(valores[2])

if a < b + c and b < a + c and c < a + b:
    perimetro = a + b + c
    print('Perimetro = {:.1f}' .format(perimetro))
else:
    area = (a + b) * c / 2
    print('Area = {:.1f}' .format(area))
