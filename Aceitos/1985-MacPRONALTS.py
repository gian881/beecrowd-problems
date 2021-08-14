# https://www.urionlinejudge.com.br/judge/pt/problems/view/1985

# O MacPRONALTS está com uma super promoção, exclusivo para os competidores da primeira Seletiva do MaratonaTEC. Só que teve um problema, todos os maratonistas foram tentar comprar ao mesmo tempo, com isso gerou uma fila muito grande. O pior é que a moça do caixa estava sem calculadora ou um programa para ajudá-la a calcular com maior agilidade, eis que surge você para fazer um programa para ajudar a coitada e aumentar a renda do MacPRONALTS. Segue o cardápio do dia contendo o número do produto e seu respectivo valor.
# 1001 | R$ 1.50
# 1002 | R$ 2.50
# 1003 | R$ 3.50
# 1004 | R$ 4.50
# 1005 | R$ 5.50

# Entrada
# A primeira entrada informada é a quantidade de produtos comprados (1 <= p <= 5). Para cada produto segue a quantidade (1 <= q <= 500) que o consumidor comprou.
# Obs.: não poderão ser informados números de produtos repetidos.

# Saída
# Você deve imprimir o valor da compra com duas casas decimais.

def main() -> None:
    produtos_comprados: int = int(input())
    total: float = 0.0
    precos: dict[str, float] = {"1001": 1.50,
                                "1002": 2.50,
                                "1003": 3.50,
                                "1004": 4.50,
                                "1005": 5.50}

    for _ in range(produtos_comprados):
        produto_e_quantidade: list[str] = input().strip().split()
        produto, quantidade = produto_e_quantidade[0], int(
            produto_e_quantidade[1])
        total += precos[produto] * quantidade

    print(f'{total:.2f}')


if __name__ == "__main__":
    main()
