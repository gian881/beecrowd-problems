# https://www.urionlinejudge.com.br/judge/pt/problems/view/1174

# Faça um programa que leia um vetor A[100]. No final, mostre todas as posições do vetor que armazenam um valor menor ou igual a 10 e o valor armazenado em cada uma das posições.

# Entrada
# A entrada contém 100 valores, podendo ser inteiros, reais, positivos ou negativos.

# Saída
# Para cada valor do vetor menor ou igual a 10, escreva "A[i] = x", onde i é a posição do vetor e x é o valor armazenado na posição, com uma casa após o ponto decimal.

def main() -> None:
    vetor: list[float] = [0.0 for _ in range(100)]

    for i in range(100):
        numero = float(input())
        vetor[i] = numero
    for indice, valor in enumerate(vetor):
        if valor <= 10:
            print(f'A[{indice}] = {valor}')


if __name__ == "__main__":
    main()
