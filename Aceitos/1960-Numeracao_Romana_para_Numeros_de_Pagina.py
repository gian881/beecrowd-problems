# https://www.beecrowd.com.br/judge/pt/problems/view/1960

# A ECI (Editio Chronica Incredibilis ou Editora de Crônicas Incríveis) é muito tradicional quando se trata de numerar as páginas de seus livros. Ela sempre usa a numeração romana para isso. E seus livros nunca ultrapassam as 999 páginas pois, quando necessário, dividem o livro em volumes.
# Você deve escrever um programa que, dado um número arábico, mostra seu equivalente na numeração romana.
# Lembre que I representa 1, V é 5, X é 10, L é 50, C é 100, D é 500 e M representa 1000.

# Entrada
# A entrada é um número inteiro positivo N (0 < N < 1000).

# Saída
# A saída é o número N escrito na numeração romana em uma única linha. Use sempre letras maiúsculas.

def main() -> None:
    numero: int = int(input())
    numeros: list[int] = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    simbolos: list[str] = ['I', 'IV', 'V', 'IX', 'X',
                           'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    i = len(numeros) - 1

    while numero:
        div, numero = divmod(numero, numeros[i])
        for _ in range(div):
            print(simbolos[i], end='')

        i -= 1


if __name__ == "__main__":
    main()
