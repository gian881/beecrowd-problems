# https://www.beecrowd.com.br/judge/pt/problems/view/1158

# Leia um valor inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste de dois inteiros X e Y. Você deve apresentar a soma de Y ímpares consecutivos a partir de X inclusive o próprio X se ele for ímpar. Por exemplo:
# para a entrada 4 5, a saída deve ser 45, que é equivalente à: 5 + 7 + 9 + 11 + 13
# para a entrada 7 4, a saída deve ser 40, que é equivalente à: 7 + 9 + 11 + 13

# Entrada
# A primeira linha de entrada é um inteiro N que é a quantidade de casos de teste que vem a seguir. Cada caso de teste consiste em uma linha contendo dois inteiros X e Y.

# Saída
# Imprima a soma dos consecutivos números ímpares a partir do valor X.

def main() -> None:

    n = int(input())
    valor = 0

    for i in range(n):
        valores = input().strip().split()

        x = int(valores[0])
        y = int(valores[1])
        s = 0

        for j in range(y):
            while x % 2 == 0:
                x += 1
            s += x
            x += 1
        print(s)


if __name__ == "__main__":
    main()
