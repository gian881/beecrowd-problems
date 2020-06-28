c = int(input())

for i in range(c):
    a = input().strip().split()

    nome = a[0]

    if nome == 'Thor':
        print('Y')
    else:
        print('N')
