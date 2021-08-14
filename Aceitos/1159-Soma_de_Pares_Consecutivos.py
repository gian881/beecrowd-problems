# https://www.urionlinejudge.com.br/judge/pt/problems/view/1159

# O programa deve ler um valor inteiro X indefinidas vezes. (O programa irá parar quando o valor de X for igual a 0). Para cada X lido, imprima a soma dos 5 pares consecutivos a partir de X, inclusive o X , se for par. Se o valor de entrada for 4, por exemplo, a saída deve ser 40, que é o resultado da operação: 4+6+8+10+12, enquanto que se o valor de entrada for 11, por exempo, a saída deve ser 80, que é a soma de 12+14+16+18+20.

# Entrada
# O arquivo de entrada contém muitos valores inteiros. O último valor do arquivo é zero.

# Saída
# Imprima a saida conforme a explicação acima e o exemplo abaixo.

def main() -> None:

    def soma5Pares(x: int) -> int:
        soma = 0
        for i in range(x, x+10):
            if i % 2 == 0:
                soma += i
        return soma

    while True:
        numero = int(input())
        if numero == 0:
            break
        else:
            print(soma5Pares(numero))


if __name__ == "__main__":
    main()
