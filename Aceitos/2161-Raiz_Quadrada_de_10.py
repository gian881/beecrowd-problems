# https://www.urionlinejudge.com.br/judge/pt/problems/view/2161

# Uma das formas de calcular a raiz quadrada de um número natural é pelo método das frações periódicas continuadas. Esse método usa como denominador uma repetição de frações. Essa repetição pode ser feita uma quantidade específica de vezes.
# Por exemplo, ao repetir 2 vezes a fração continuada para calcular a raiz quadrada de 10, temos a fórmula abaixo.
# https://resources.urionlinejudge.com.br/gallery/images/contests/933.png
# Sua tarefa é, dado o número N de repetições, calcular o valor aproximado da raiz quadrada de 10.

# Entrada
# A entrada é um número natural N (0 ≤ N ≤ 100), que indica o número de repetições do denominador na fração continuada.

# Saída
# A saída é o valor aproximado da raiz quadrada com 10 casas decimais.

def main() -> None:
    repeticoes: int = int(input())
    resultado: float = 0

    for _ in range(repeticoes):
        resultado += 6
        resultado = 1/resultado

    resultado += 3
    print(f'{resultado:.10f}')


if __name__ == "__main__":
    main()
