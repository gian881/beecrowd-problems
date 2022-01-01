# https://www.beecrowd.com.br/judge/pt/problems/view/1113

# Leia uma quantidade indeterminada de duplas de valores inteiros X e Y. Escreva para cada X e Y uma mensagem que indique se estes valores foram digitados em ordem crescente ou decrescente.

# Entrada
# A entrada contém vários casos de teste. Cada caso contém dois valores inteiros X e Y. A leitura deve ser encerrada ao ser fornecido valores iguais para X e Y.

# Saída
# Para cada caso de teste imprima “Crescente”, caso os valores tenham sido digitados na ordem crescente, caso contrário imprima a mensagem “Decrescente”.

def main() -> None:

    while True:
        valores = input().strip().split()

        x = int(valores[0])
        y = int(valores[1])

        if x == y:
            break

        if x < y:
            print('Crescente')
        else:
            print('Decrescente')


if __name__ == "__main__":
    main()
