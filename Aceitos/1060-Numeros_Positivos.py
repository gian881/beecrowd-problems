# https://www.beecrowd.com.br/judge/pt/problems/view/1060

# Faça um programa que leia 6 valores. Estes valores serão somente negativos ou positivos (desconsidere os valores nulos). A seguir, mostre a quantidade de valores positivos digitados.

# Entrada
# Seis valores, negativos e/ou positivos.

# Saída
# Imprima uma mensagem dizendo quantos valores positivos foram lidos.

def main() -> None:
    pos = 0
    for i in range(0, 6):
        valor = float(input())
        if valor > 0:
            pos += 1
    print('{} valores positivos' .format(pos))


if __name__ == "__main__":
    main()
