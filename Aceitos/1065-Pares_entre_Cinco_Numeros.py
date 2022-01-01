# https://www.beecrowd.com.br/judge/pt/problems/view/1065

# Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.

# Entrada
# O arquivo de entrada contém 5 valores inteiros quaisquer.

# Saída
# Imprima a mensagem conforme o exemplo fornecido, indicando a quantidade de valores pares lidos.

def main() -> None:
    par = 0
    for i in range(0, 5):
        num = int(input())
        if num % 2 == 0:
            par += 1
    print('{} valores pares' .format(par))


if __name__ == "__main__":
    main()
