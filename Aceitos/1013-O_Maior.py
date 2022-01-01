# https://www.beecrowd.com.br/judge/pt/problems/view/1013

# Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”.
# Utilize a fórmula:
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1013.png

# Entrada
# O arquivo de entrada contém três valores inteiros.

# Saída
# Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

def main() -> None:
    maior: int = max(int(valor) for valor in input().strip().split())

    print(f'{maior} eh o maior')


if __name__ == "__main__":
    main()
