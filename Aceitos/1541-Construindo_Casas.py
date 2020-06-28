while True:
    v = input().strip().split()
    if len(v) == 1 and v[0] == '0':
        break
    else:
        a, b, c = int(v[0]), int(v[1]), int(v[2])
        pc = c / 100
        x = (a * b / pc)**0.5
        print(int(x))
