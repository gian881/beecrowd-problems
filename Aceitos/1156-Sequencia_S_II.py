# https://www.urionlinejudge.com.br/judge/pt/problems/view/1156

# Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
# S = 1 + 3/2 + 5/4 + 7/8 + ... + 39/?

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# A saída contém um valor correspondente ao valor de S.
# O valor deve ser impresso com dois dígitos após o ponto decimal.

def main() -> None:

    def main() -> None:
        soma: float = 1
        a: float = 3
        b: float = 2
        for _ in range(19):
            soma += a / b
            a += 2
            b *= 2

        print(f'{soma:.2f}')

    if __name__ == "__main__":
        main()


if __name__ == "__main__":
    main()
