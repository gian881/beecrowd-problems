# https://www.urionlinejudge.com.br/judge/pt/problems/view/1132

# Escreva um algoritmo que leia 2 valores inteiros X e Y calcule a soma dos números que não são múltiplos de 13 entre X e Y, incluindo ambos.

# Entrada
# O arquivo de entrada contém 2 valores inteiros quaisquer, não necessariamente em ordem crescente.

# Saída
# Imprima a soma de todos os valores não divisíveis por 13 entre os dois valores lidos na entrada, inclusive ambos se for o caso.

def main() -> None:

    soma = 0
    x = int(input())
    y = int(input())

    lista = [x, y]
    lista = sorted(lista)

    x = lista[0]
    y = lista[1]

    for i in range(x, y + 1):
        if i % 13 != 0:
            soma += i
    print(soma)


if __name__ == "__main__":
    main()
