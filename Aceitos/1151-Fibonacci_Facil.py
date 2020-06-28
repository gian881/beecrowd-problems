t = int(input())
a = 0
b = 1
print('{} {} ' .format(a, b), end='')
counter = 3
while counter <= t:
    c = a + b
    if counter < t:
        print('{} ' .format(c), end='')
    else:
        print('{}' .format(c))
    a = b
    b = c
    counter += 1
