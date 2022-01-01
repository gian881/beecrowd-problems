# https://www.beecrowd.com.br/judge/pt/problems/view/1038

# Com base na tabela abaixo, escreva um programa que leia o código de um item e a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1038_pt.png

# Entrada
# O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

# Saída
# O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.

def main() -> None:
    valores = input().strip().split()

    codigo = int(valores[0])
    quant = int(valores[1])
    valor: float = 4.0

    if codigo == 2:
        valor = 4.5
    elif codigo == 3:
        valor = 5.0
    elif codigo == 4:
        valor = 2.0
    elif codigo == 5:
        valor = 1.5

    total = quant * valor

    print('Total: R$ {:.2f}' .format(total))


if __name__ == "__main__":
    main()
