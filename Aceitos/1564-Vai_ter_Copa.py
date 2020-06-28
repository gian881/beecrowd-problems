while True:
    try:
        r = int(input())
        if r == 0:
            print('vai ter copa!')
        elif r > 0:
            print('vai ter duas!')
    except EOFError:
        break
