# https://www.urionlinejudge.com.br/judge/pt/problems/view/1021

# Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.

# Entrada
# O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).

# Saída
# Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
# Obs: Utilize ponto (.) para separar a parte decimal.

def main() -> None:

    money = float(input())
    money += 0.001

    print('NOTAS:')
    notas = money // 100
    money %= 100
    print('{:.0f} nota(s) de R$ 100.00' .format(notas))

    notas = money // 50
    money %= 50
    print('{:.0f} nota(s) de R$ 50.00' .format(notas))

    notas = money // 20
    money %= 20
    print('{:.0f} nota(s) de R$ 20.00' .format(notas))

    notas = money // 10
    money %= 10
    print('{:.0f} nota(s) de R$ 10.00' .format(notas))

    notas = money // 5
    money %= 5
    print('{:.0f} nota(s) de R$ 5.00' .format(notas))

    notas = money // 2
    money %= 2
    print('{:.0f} nota(s) de R$ 2.00' .format(notas))

    print('MOEDAS:')
    moedas = money // 1
    money %= 1
    print('{:.0f} moeda(s) de R$ 1.00' .format(moedas))

    moedas = money // 0.5
    money %= 0.5
    print('{:.0f} moeda(s) de R$ 0.50' .format(moedas))

    moedas = money // 0.25
    money %= 0.25
    print('{:.0f} moeda(s) de R$ 0.25' .format(moedas))

    moedas = money // 0.1
    money %= 0.1
    print('{:.0f} moeda(s) de R$ 0.10' .format(moedas))

    moedas = money // 0.05
    money %= 0.05
    print('{:.0f} moeda(s) de R$ 0.05' .format(moedas))

    moedas = money // 0.01
    money %= 0.01
    print('{:.0f} moeda(s) de R$ 0.01' .format(moedas))
    print()


if __name__ == "__main__":
    main()
