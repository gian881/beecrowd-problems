# https://www.urionlinejudge.com.br/judge/pt/problems/view/1042

# Leia 3 valores inteiros e ordene-os em ordem crescente. No final, mostre os valores em ordem crescente, uma linha em branco e em seguida, os valores na sequência como foram lidos.

# Entrada
# A entrada contem três números inteiros.

# Saída
# Imprima a saída conforme foi especificado.

def main() -> None:

    valores = [int(numero) for numero in input().strip().split()]
    a, b, c = valores
    lista = [a, b, c]
    lista_sorted = sorted(valores)

    for i in lista_sorted:
        print(i)

    print()

    for i in lista:
        print(i)


if __name__ == "__main__":
    main()
