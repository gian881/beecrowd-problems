a = 12
soma = 0
M = []

coluna = int(input())
op = input().upper().strip()  # SOMA OU MEDIA

for i in range(a):
    linha = []
    for j in range(a):
        valor = float(input())
        linha.append(valor)
    M.append(linha)

for x in range(a):
    for y in range(a):
        if y == coluna:
            soma += M[x][y]

if op == 'S':
    print('{:.1f}' .format(soma))

if op == 'M':
    print('{:.1f}' .format(soma / a))
