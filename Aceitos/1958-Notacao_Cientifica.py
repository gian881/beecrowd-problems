# https://www.beecrowd.com.br/judge/pt/problems/view/1958

# Números em ponto flutuante podem ser bastante extensos para mostrar. Nesses casos, é conveniente usar a notação científica.
# Você deve escrever um programa que, dado um número em ponto flutuante, mostre este número na notação científica: sempre mostre o sinal da mantissa; sempre mostre 4 casas decimais na mantissa; use o caractere 'E' para separar a mantissa do expoente; sempre mostre o sinal do expoente; e mostre o expoente com pelo menos 2 dígitos.

# Entrada
# A entrada é um número em ponto flutuante de dupla precisão X (de acordo com o padrão IEEE 754-2008). Nunca haverá um número com mais de 110 caracteres nem com mais de 6 casas decimais.

# Saída
# A saída é o número X em uma única linha na notação científica detalhada acima. Veja os exemplos abaixo.

def main() -> None:
    numero: float = float(input())
    resultado: str = ''

    divisoes = 0

    resultado += '-' if numero < 0 else '+'

    while True:
        if len(str(numero).split('.')[0]) == 1:
            break

        numero /= 10
        divisoes += 1

    resultado += f'{numero:.4f}E{str(divisoes).zfill(2)}'
    print(resultado)


if __name__ == "__main__":
    main()
