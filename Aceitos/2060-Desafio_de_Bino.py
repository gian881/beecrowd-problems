# https://www.beecrowd.com.br/judge/pt/problems/view/2060

# Bino e Cino são colegas inseparáveis. Bino gosta de criar desafios matemáticos para Cino resolver. Desta vez, Bino gerou uma lista de números e perguntou ao Cino quantos números da lista são múltiplos de 2, 3, 4 e 5.
# Esse desafio pode parecer simples, porém, quando a lista contém muitos números, Cino se confunde e acaba errando alguns cálculos. Para ajudar Cino, faça um programa para resolver o desafio de Bino.

# Entrada
# A primeira linha da entrada consiste em um inteiro N (1 ≤ N ≤1000), representando a quantidade de números na lista de Bino.
# A segunda linha contém N inteiros Li (1 ≤ Li ≤ 100), representando os números da lista de Bino.

# Saída
# Imprima a quantidade de números múltiplos de 2, 3, 4 e 5 presentes na lista. Observe a formatação da saída nos exemplos, pois ela deve ser seguida rigorosamente.

def main() -> None:
    mult_2 = mult_3 = mult_4 = mult_5 = 0

    _ = input()
    numeros: list[int] = [int(numero) for numero in input().split()]

    for numero in numeros:
        if numero % 2 == 0:
            mult_2 += 1
        if numero % 3 == 0:
            mult_3 += 1
        if numero % 4 == 0:
            mult_4 += 1
        if numero % 5 == 0:
            mult_5 += 1

    print(f'{mult_2} Multiplo(s) de 2')
    print(f'{mult_3} Multiplo(s) de 3')
    print(f'{mult_4} Multiplo(s) de 4')
    print(f'{mult_5} Multiplo(s) de 5')


if __name__ == "__main__":
    main()
