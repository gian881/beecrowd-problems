def checkFeliz(a, b, c):
    if a > b and b >= c:
        return True
    elif a < b and b >= c:
        return False
    elif a < b and b < c and c - b < b - a:
        return False
    elif a < b and b < c and c - b == b - a:
        return True
    elif a > b and b > c and c - b < b - a:
        return True
    elif a > b and b > c and c - b == b - a:
        return False
    elif a == b and b < c:
        return True
    elif a == b and b > c:
        return False
    elif a == b == c:
        return False


a, b, c = input().strip().split()
a, b, c = int(a), int(b), int(c)

if checkFeliz(a, b, c) is True:
    resposta = ':)'
else:
    resposta = ':('

print(resposta)
