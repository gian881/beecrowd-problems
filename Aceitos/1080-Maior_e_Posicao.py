# https://www.urionlinejudge.com.br/judge/pt/problems/view/1080

# Leia 100 valores inteiros. Apresente então o maior valor lido e a posição dentre os 100 valores lidos.

# Entrada
# O arquivo de entrada contém 100 números inteiros, positivos e distintos.

# Saída
# Apresente o maior valor lido e a posição de entrada, conforme exemplo abaixo.

def main() -> None:

    lista = []
    maior = 0

    for i in range(0, 100):
        a = int(input())
        if a > maior:
            maior = a
        lista.append(a)

    print(maior)
    print(lista.index(maior) + 1)


if __name__ == "__main__":
    main()
