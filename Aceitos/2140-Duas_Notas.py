# https://www.beecrowd.com.br/judge/pt/problems/view/2140

# Gilberto é um famoso vendedor de esfirras na região. Porém, apesar de todos gostarem de suas esfirras, ele só sabe dar o troco com duas notas, ou seja, nem sempre é possível receber o troco certo. Para facilitar a vida de Gil, escreva um programa para ele que determine se é possível ou não devolver o troco exato utilizando duas notas.
# As notas disponíveis são: 2, 5, 10, 20, 50 e 100.

# Entrada
# A entrada deve conter o valor inteiro N da compra realizada pelo cliente e, em seguida, o valor inteiro M pago pelo cliente (N < M ≤ 104). A entrada termina com N = M = 0.

# Saída
# Seu programa deverá imprimir "possible" se for possível devolver o troco exato ou "impossible" se não for possível.

def main() -> None:
    notas_disponiveis: list[int] = [2, 5, 10, 20, 50, 100]
    trocos_possiveis: set[int] = {
        nota1 + nota2 for nota1 in notas_disponiveis for nota2 in notas_disponiveis}

    while True:
        preco, valor_pago = [int(valor) for valor in input().split()]
        if preco == valor_pago == 0:
            break
        troco = valor_pago - preco
        if troco in trocos_possiveis:
            print('possible')
        else:
            print('impossible')


if __name__ == "__main__":
    main()
