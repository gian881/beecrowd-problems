# https://www.beecrowd.com.br/judge/pt/problems/view/2162

# Ao observar a paisagem da Nlogônia, o professor MC percebeu que a cada intervalo de 100 metros existe um pico. E que exatamente na metade de dois picos há um vale. Logo, a cada 50 metros há um vale ou um pico e, ao longo da paisagem, não há um pico seguido por outro pico, nem um vale seguido por outro vale.
# O professor MC ficou curioso com esse padrão e quer saber se, ao medir outras paisagens, isso se repete. Sua tarefa é, dada uma paisagem, indicar se ela possui esse padrão ou não.

# Entrada
# A entrada é dada em duas linhas. A primeira tem o número N de medidas da paisagem (1 < N ≤ 100). A segunda linha tem N inteiros: a altura Hi de cada medida (-10000 ≤ Hi ≤ 10000, para todo Hi, tal que 1 ≤ i ≤ N). Uma medida é considerada um pico se é maior que a medida anterior. Uma medida é considerada um vale se é menor que a medida anterior.

# Saída
# A saída é dada em uma única linha. Caso a paisagem tenha o mesmo padrão da Nlogônia, deve ser mostrado o número 1. Caso contrário, mostra-se o número 0.

def main() -> int:
    casos: int = int(input())

    numeros: list[int] = [int(numero) for numero in input().split()]

    if len(numeros) == 1:

        return 1
    if len(numeros) == 2 and numeros[0] == numeros[1]:

        return 0

    pico: bool = numeros[0] < numeros[1]

    for idx, num in enumerate(numeros[1:], 1):
        if idx != casos - 1:
            proximo: int = numeros[idx + 1]
            if pico and num <= proximo:

                return 0
            if not pico and num >= proximo:

                return 0
        pico = not pico
    return 1


if __name__ == "__main__":
    print(main())
