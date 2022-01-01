# https://www.beecrowd.com.br/judge/pt/problems/view/1154

# Faça um algoritmo para ler um número indeterminado de dados, contendo cada um, a idade de um indivíduo. O último dado, que não entrará nos cálculos, contém o valor de idade negativa. Calcular e imprimir a idade média deste grupo de indivíduos.

# Entrada
# A entrada contém um número indeterminado de inteiros. A entrada será encerrada quando um valor negativo for lido.

# Saída
# A saída contém um valor correspondente à média de idade dos indivíduos.
# A média deve ser impressa com dois dígitos após o ponto decimal.

def main() -> None:

    soma = 0
    pessoas = 0
    while True:
        idade = int(input())

        if idade > 0:
            soma += idade
            pessoas += 1
        if idade < 0:
            break
    media = soma / pessoas
    print('{:.2f}'.format(media))


if __name__ == "__main__":
    main()
