# https://www.beecrowd.com.br/judge/pt/problems/view/2126

# Dados dois números naturais N1 e N2, diz-se que N1 é subsequência contígua de N2 se todos os dígitos de N1 aparecem, na mesma ordem e de forma contígua, em N2. Crie uma aplicação que leia dois números naturais e diga se o primeiro é uma subsequência contígua do segundo.

# Entrada
# A entrada é composta por vários casos de teste e termina com final de arquivo (EOF). A primeira linha de cada entrada é composta por um valor natural  N1(1 < N1 < 1010), a segunda linha é composta por um valor N2( N1 < N2 < 1032).

# Saída
# Para cada caso de teste imprima a quantidade de subsequências contíguas e a posição onde a subsequência é iniciada, caso exista mais de uma subsequência, imprima onde é iniciada a última subsequência. Caso não exista subsequência, imprima "Nao existe subsequencia". Mostre o resultado conforme o exemplo de saída.

def main() -> None:
    caso: int = 1
    while True:
        try:
            numero1: str = input()
            numero2: str = input()
            print(f'Caso #{caso}:')
            if numero1 not in numero2:
                print(f'Nao existe subsequencia')
            else:
                subsequencias: int = 0
                comeco: int = 0

                while numero1 in numero2:
                    comeco = numero2.find(numero1)
                    numero2 = numero2[:comeco] + '-' * \
                        len(numero1) + numero2[comeco + len(numero1):]
                    subsequencias += 1

                print(f'Qtd.Subsequencias: {subsequencias}')
                print(f'Pos: {comeco + 1}')
            print()
            caso += 1
        except EOFError:
            break


if __name__ == "__main__":
    main()
