# https://www.urionlinejudge.com.br/judge/pt/problems/view/1155

# Escreva um algoritmo para calcular e escrever o valor de S, sendo S dado pela fórmula:
# S = 1 + 1/2 + 1/3 + … + 1/100

# Entrada
# Não há nenhuma entrada neste problema.

# Saída
# A saída contém um valor correspondente ao valor de S.
# O valor deve ser impresso com dois dígitos após o ponto decimal.

def main() -> None:

    def main() -> None:
        soma: float = 0
        for i in range(1, 101):
            soma += 1 / i
        print(f'{soma:.2f}')

    if __name__ == "__main__":
        main()


if __name__ == "__main__":
    main()
