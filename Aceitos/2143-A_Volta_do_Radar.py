# https://www.urionlinejudge.com.br/judge/pt/problems/view/2143

# Todo ano após a competição que ocorre na cidade de Taxilândia, os participantes e os coaches vão para o célebre restaurante Radar. Porém, os garçons (sempre muito gentis e educados) ficam sobrecarregados devido à quantidade de pessoas, e consequentemente, acabam demorando um pouco para atender a um pedido.
# Os participantes ou coaches que sentam nas pontas são os privilegiados, pois são atendidos com somente um pedido, mas os demais precisam sempre pedir duas vezes, pois os garçons (apesar de gentis e educados) são desatentos e se esquecem facilmente dos pedidos. Além disso, há uma superstição entre os participantes e coaches de que se não houver um número par de pessoas que não sentam nas pontas, na próxima competição nenhuma equipe da universidade conseguirá vencer.
# Portanto, sua tarefa é determinar a soma da quantidade de pedidos de cada um para saber se vale a pena ir ao Radar. Mas apesar do resultado, lembre-se: sempre vale a pena ir ao Radar!

# Entrada
# A entrada é composta por T (1 ≤ T ≤ 100) indicando a quantidade de casos de teste e então, T inteiros N (3 ≤ N ≤ 104), indicando a quantidade de pessoas. A mesa é retangular e haverá pelo menos e no máximo uma pessoa em uma das pontas, isto é, se uma ponta estiver vazia, a outra deve ser ocupada, ou senão, as duas pontas estarão ocupadas, mas o número de pessoas que não estão nas pontas sempre será par. O final da entrada é indicado por T = 0.

# Saída
# Seu programa deverá imprimir a soma da quantidade de pedidos de cada pessoa. Não haverá linha em branco entre os casos de teste.

def calular_pedidos() -> None:
    ponta: int
    resto: int

    pessoas: int = int(input())
    ponta = 2 if pessoas % 2 == 0 else 1
    resto = pessoas - ponta
    pedidos = ponta + resto * 2
    print(pedidos)


def main() -> None:
    while True:
        casos: int = int(input())
        if casos == 0:
            break
        for _ in range(casos):
            calular_pedidos()


if __name__ == "__main__":
    main()