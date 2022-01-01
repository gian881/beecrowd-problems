# https://www.beecrowd.com.br/judge/pt/problems/view/2168

# No crepúsculo, a cidade de Portland fica cheia de vampiros e lobisomens. Entretanto, nenhum deles quer ser visto enquanto passeiam pelo centro.
# Vão ser instaladas câmeras de vigilância em cada esquina do centro de Portland. A cada mês, um mapa atualizado com as câmeras já em funcionamento é disponibilizado no site da prefeitura.
# Uma quadra é considerada segura se existem câmeras em, pelo menos, duas de suas quatro esquinas. No centro de Portland todas as quadras são quadrados de mesmo tamanho.
# Sua tarefa é, dado o mapa das câmeras em funcionamento nas esquinas, indicar o status de todas as quadras do centro.

# Entrada
# A primeira linha da entrada tem um inteiro positivo N (1 ≤ N ≤ 100). Nas próximas N+1 linhas, existem N+1 números, que indicam, para cada esquina, a presença ou ausência de uma câmera de vigilância em funcionamento. O número 1 indica que existe uma câmera funcionando na esquina, enquanto o número zero indica que não há câmera funcionando.

# Saída
# A saída é dada em N linhas. Cada linha tem N caracteres, indicando se a quadra correspondente é segura ou insegura. Se uma quadra é segura, mostre o caractere S; se não é segura, mostre o caractere U.

def main() -> None:
    tamanho_matriz: int = int(input())
    matriz: list[list[int]] = [
        [int(numero) for numero in input().split()] for _ in range(tamanho_matriz + 1)]

    for y, linha in enumerate(matriz):
        if y != tamanho_matriz:
            for x in range(len(linha)):
                if x != tamanho_matriz:
                    cameras: int = 0
                    for i in range(y, y + 2):
                        for j in range(x, x + 2):
                            numero = matriz[i][j]
                            if numero:
                                cameras += 1
                    print('S' if cameras >= 2 else 'U', end='')
            print('\n', end='')


if __name__ == "__main__":
    main()
