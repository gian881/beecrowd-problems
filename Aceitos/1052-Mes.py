# https://www.urionlinejudge.com.br/judge/pt/problems/view/1052

# Leia um valor inteiro entre 1 e 12, inclusive. Correspondente a este valor, deve ser apresentado como resposta o mês do ano por extenso, em inglês, com a primeira letra maiúscula.

# Entrada
# A entrada contém um único valor inteiro.

# Saída
# Imprima por extenso o nome do mês correspondente ao número existente na entrada, com a primeira letra em maiúscula.

def main() -> None:
    meses = ['January', 'February', 'March', 'April', 'May', 'June',
             'July', 'August', 'September', 'October', 'November', 'December']
    mes = int(input())

    print(meses[mes - 1])


if __name__ == "__main__":
    main()
