# https://www.urionlinejudge.com.br/judge/pt/problems/view/1044

# Leia 2 valores inteiros (A e B). Após, o programa deve mostrar uma mensagem "Sao Multiplos" ou "Nao sao Multiplos", indicando se os valores lidos são múltiplos entre si.

# Entrada
# A entrada contém valores inteiros.

# Saída
# A saída deve conter uma das mensagens conforme descrito acima.

def main() -> None:

    valores = input().strip().split()

    a = int(valores[0])
    b = int(valores[1])

    if a % b == 0 or b % a == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')


if __name__ == "__main__":
    main()
