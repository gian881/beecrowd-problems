# https://www.urionlinejudge.com.br/judge/pt/problems/view/1071

# Leia 2 valores inteiros X e Y. A seguir, calcule e mostre a soma dos números impares entre eles.

# Entrada
# O arquivo de entrada contém dois valores inteiros.

# Saída
# O programa deve imprimir um valor inteiro. Este valor é a soma dos valores ímpares que estão entre os valores fornecidos na entrada que deverá caber em um inteiro.

def main() -> None:
    x = int(input())
    y = int(input())

    lista = [x, y]
    lista = sorted(lista)

    x = lista[0]
    y = lista[1]

    soma = 0

    for i in range(x + 1, y):
        if i % 2 != 0:
            soma += i

    print(soma)


if __name__ == "__main__":
    main()
