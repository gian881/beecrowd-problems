# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .
tempo = input().strip().split()
hri, mini, hrf, minf = tempo[0], tempo[1], tempo[2], tempo[3]

if hri == hrf and mini == minf:
    dhr = 24
    dmin = 0
elif:


print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(dhr, dmin))
