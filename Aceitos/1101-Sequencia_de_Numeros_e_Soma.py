# https://www.beecrowd.com.br/judge/pt/problems/view/1101

# Leia um conjunto não determinado de pares de valores M e N (parar quando algum dos valores for menor ou igual a zero). Para cada par lido, mostre a sequência do menor até o maior e a soma dos inteiros consecutivos entre eles (incluindo o N e M).

# Entrada
# O arquivo de entrada contém um número não determinado de valores M e N. A última linha de entrada vai conter um número nulo ou negativo.

# Saída
# Para cada dupla de valores, imprima a sequência do menor até o maior e a soma deles, conforme exemplo abaixo.

def main() -> None:

    while True:
        valores = input().strip().split()

        m = int(valores[0])
        n = int(valores[1])

        if m == 0 or n == 0 or m < 0 or n < 0:
            break

        lista = [m, n]
        lista = sorted(lista)

        soma = 0

        for i in range(lista[0], lista[1] + 1):
            print(i, end=' ')
            soma += i
        print('Sum={}' .format(soma))


if __name__ == "__main__":
    main()
