# https://www.beecrowd.com.br/judge/pt/problems/view/2313

# Dados três valores, verifique se os três podem formar um triângulo. Em caso afirmativo, verifique se ele é escaleno, isóceles ou equilátero e se trata-se de um triângulo retângulo ou não.

# Entrada
# A entrada consiste em três números inteiros A,B e C (0 < A,B,C < 105).

# Saída
# A saída deve conter a string "Invalido" se os valores lidos não formarem um triângulo. Se os valores formarem um triângulo a saída deve ser "Valido-Equilatero", "Valido-Escaleno" ou "Valido-Isoceles" de acordo com a característica do triângulo seguido de "Retangulo: S" se o triângulo for retângulo ou "Retangulo: N" se não for, conforme os exemplos.

def modulo(x):
    return x if x > 0 else -x


def main() -> None:
    a, b, c = [int(x) for x in input().split()]

    if (modulo(b - c) < a < b + c) and (modulo(a - c) < b < a + c) and (modulo(a - b) < c < a + b):
        print('Valido-', end='')
        if a == b == c:
            print('Equilatero')
        elif a == b and a != c or a == c and a != b or b == c:
            print('Isoceles')
        else:
            print('Escaleno')
        print('Retangulo: ', end='')

        if (a ** 2 == b ** 2 + c ** 2) or (b ** 2 == a ** 2 + c ** 2) or (c ** 2 == a ** 2 + b ** 2):
            print('S')
        else:
            print('N')
    else:
        print('Invalido')
        return


if __name__ == "__main__":
    main()
