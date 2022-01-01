# https://www.beecrowd.com.br/judge/pt/problems/view/1179

# Neste problema você deverá ler 15 valores colocá-los em 2 vetores conforme estes valores forem pares ou ímpares. Só que o tamanho de cada um dos dois vetores é de 5 posições. Então, cada vez que um dos dois vetores encher, você deverá imprimir todo o vetor e utilizá-lo novamente para os próximos números que forem lidos. Terminada a leitura, deve-se imprimir o conteúdo que restou em cada um dos dois vetores, imprimindo primeiro os valores do vetor impar. Cada vetor pode ser preenchido tantas vezes quantas for necessário.

# Entrada
# A entrada contém 15 números inteiros.

# Saída
# Imprima a saída conforme o exemplo abaixo.

def main() -> None:

    par: list[int] = []
    impar: list[int] = []

    for _ in range(15):
        valor = int(input())

        if valor % 2 == 0:
            par.append(valor)
        else:
            impar.append(valor)

        if len(par) == 5:
            for index_par, valor_par in enumerate(par):
                print(f'par[{index_par}] = {valor_par}')
            par = []
        if len(impar) == 5:
            for index_impar, valor_impar in enumerate(impar):
                print(f'impar[{index_impar}] = {valor_impar}')
            impar = []

    for index_impar_1, valor_impar_1 in enumerate(impar):
        print(f'impar[{index_impar_1}] = {valor_impar_1 }')

    for index_par_1, valor_par_1 in enumerate(par):
        print(f'par[{index_par_1 }] = {valor_par_1 }')


if __name__ == "__main__":
    main()
