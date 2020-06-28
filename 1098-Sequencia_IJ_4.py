from decimal import Decimal
i = 0
j = 1
cont = 0

while cont < 33:

    print('I={} J={}' .format(i, j))
    cont += 1
    if cont % 3 == 0:
        i += Decimal('0.2')
        j -= 2
        j += Decimal('0.2')
    else:
        j += 1
