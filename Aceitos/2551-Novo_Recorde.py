# https://www.beecrowd.com.br/judge/pt/problems/view/2551

# A grande Maratona de Rua de Curitiba irá ocorrer nos próximos dias! Vários atletas estão treinando há dias para o grande dia da corrida. Flávio é um dos atletas que está treinando diariamente para se sair bem na corrida. Ele tem corrido todas as manhãs nas pistas próximas de sua casa.
# Os treinos do garoto são monitorados por um aplicativo em seu celular. Após cada treino, Flávio sabe tanto a duração do treino quanto a distância total percorrida. Com essas informações, ele consegue determinar a velocidade média obtida em cada treino.
# Flávio está muito preocupado com a evolução de seu desempenho nos treinos, e em particular com seu recorde de velocidade média. Tal recorde é batido em um dado treino quando a velocidade média para este treino é maior que todas as velocidades médias obtidas nos treinos anteriores. Ajude Flávio a determinar em quais treinos ele conseguiu bater seu recorde.

# Entrada
# A entrada contém vários casos de teste. A primeira linha de cada caso contém um inteiro N (1 ≤ N ≤ 30), o número de treinos feitos. Considere que os treinos foram feitos nos dias 1, 2,...,N. As próximas N linhas descrevem os treinos. A linha i (1 ≤ i ≤ N) contém dois inteiros Ti e Di (1 ≤ Ti, Di ≤ 100), indicando, respectivamente, a duração do treino (em minutos) e a distância percorrida no treino (em quilômetros).
# A entrada termina com fim-de-arquivo (EOF).

# Saída
# Para cada caso de teste, imprima uma lista de inteiros indicando os dias nos quais o recorde foi batido. Cada dia deve ser impresso em uma linha. Imprima os dias em ordem crescente. Note que o dia 1 sempre deve ser impresso.

def main() -> None:
    while True:
        try:
            treinos = int(input())
            recorde: float = 0
            for dia in range(1, treinos+1):
                tempo, distancia = map(int, input().split())
                velocidade = distancia / tempo
                if velocidade > recorde:
                    recorde = velocidade
                    print(dia)
        except EOFError:
            break


if __name__ == "__main__":
    main()
