# https://www.beecrowd.com.br/judge/pt/problems/view/1175

# Faça um programa que leia um vetor N[20]. Troque a seguir, o primeiro elemento com o último, o segundo elemento com o penúltimo, etc., até trocar o 10º com o 11º. Mostre o vetor modificado.

# Entrada
# A entrada contém 20 valores inteiros, positivos ou negativos.

# Saída
# Para cada posição do vetor N, escreva "N[i] = Y", onde i é a posição do vetor e Y é o valor armazenado naquela posição.

def main() -> None:
    lista: list[int] = []

    for _ in range(20):
        numero = int(input())
        lista.append(numero)

    lista.reverse()

    for indice, valor in enumerate(lista):
        print(f'N[{indice}] = {valor}')


if __name__ == "__main__":
    main()
