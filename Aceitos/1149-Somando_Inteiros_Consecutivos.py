# https://www.beecrowd.com.br/judge/pt/problems/view/1149

# Faça um algoritmo para ler um valor A e um valor N. Imprimir a soma de A + i para cada i com os valores (0 <= i <= N-1). Enquanto N for negativo ou ZERO, um novo N(apenas N) deve ser lido.

# Entrada
# A entrada contém somente valores inteiros, podendo ser positivos ou negativos. Todos os valores estão na mesma linha.

# Saída
# A saída contém apenas um valor inteiro.

def main() -> None:

    ler = input().split()
    inicial, final, *resto = [int(num) for num in ler]

    if final <= 0:
        for numero in resto:
            final = numero
            if final > 0:
                break
    soma = 0

    itens = [i for i in range(final)]

    for item in itens:
        soma += inicial + item

    print(soma)


if __name__ == "__main__":
    main()
