a = 12
soma = 0
M = []  # copiado

line = int(input())
op = input().upper().strip()  # SOMA OU MEDIA

for i in range(a):
    linha = []  # copiado
    for j in range(a):
        valor = float(input())
        linha.append(valor)  # copiado
    M.append(linha)  # copiado

for b in M[line]:
    soma += b

if op == 'S':
    print('{:.1f}' .format(soma))

if op == 'M':
    print('{:.1f}' .format(soma / a))
