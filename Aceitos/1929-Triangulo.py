# https://www.urionlinejudge.com.br/judge/pt/problems/view/1929

# Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos, numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas, não dá para formar o triângulo.
# Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.

# Entrada
# A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100).

# Saída
# Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser ‘S’ caso seja possível formar o triângulo, ou ‘N’ caso não seja possível formar o triângulo.

def main() -> None:

    def checkTriangle(a, b, c):
        return a < b + c and b < c + a and c < a + b

    def main() -> None:
        a, b, c, d = [int(numero) for numero in input().strip().split()]

        if checkTriangle(a, b, c) or checkTriangle(a, b, d) or checkTriangle(a, c, d) or checkTriangle(b, c, d):
            print('S')
        else:
            print('N')

    if __name__ == "__main__":
        main()


if __name__ == "__main__":
    main()
