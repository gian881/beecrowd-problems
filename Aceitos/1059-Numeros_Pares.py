# https://www.beecrowd.com.br/judge/pt/problems/view/1059

# Faça um programa que mostre os números pares entre 1 e 100, inclusive.

# Entrada
# Neste problema extremamente simples de repetição não há entrada.

# Saída
# Imprima todos os números pares entre 1 e 100, inclusive se for o caso, um em cada linha.

def main() -> None:
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)


if __name__ == "__main__":
    main()
