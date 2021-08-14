# https://www.urionlinejudge.com.br/judge/pt/problems/view/2164

# A fórmula de Binet é uma forma de calcular números de Fibonacci.
# https://resources.urionlinejudge.com.br/gallery/images/contests/944.png
# Sua tarefa é, dado um natural n, calcular o valor de Fibonacci(n) usando a fórmula acima.

# Entrada
# A entrada é um número natural n (0 < n ≤ 50).

# Saída
# A saída é o valor de Fibonacci(n) com 1 casa decimal utilizando a fórmula de Binet dada.
import math


def fibonacci(numero: int) -> float:
    part1: float = math.pow((1 + math.sqrt(5)) / 2, numero)
    part2: float = math.pow((1 - math.sqrt(5)) / 2, numero)
    return (part1 - part2) / math.sqrt(5)


def main() -> None:
    numero: int = int(input())
    print(f'{fibonacci(numero):.1f}')


if __name__ == "__main__":
    main()
