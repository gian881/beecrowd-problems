# https://www.beecrowd.com.br/judge/pt/problems/view/1047

# Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
# Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.

# Entrada
# Quatro números inteiros representando a hora de início e fim do jogo.

# Saída
# Mostre a seguinte mensagem: “O JOGO DUROU XXX HORA(S) E YYY MINUTO(S)” .

def main() -> None:
    lista = [int(x) for x in input().split()]
    hora_inicial, minuto_inicial, hora_final, minuto_final = lista

    duracao_hora: int = 0
    duracao_min: int = 0

    if hora_inicial == hora_final and minuto_inicial >= minuto_final:
        duracao_hora = 24

    if hora_inicial > hora_final:
        duracao_hora = 24 - hora_inicial + hora_final

    if hora_inicial < hora_final:
        duracao_hora = hora_final - hora_inicial

    if minuto_inicial > minuto_final:
        duracao_hora -= 1
        duracao_min = 60 - minuto_inicial + minuto_final

    if minuto_inicial < minuto_final:
        duracao_min = minuto_final - minuto_inicial

    print(f'O JOGO DUROU {duracao_hora} HORA(S) E {duracao_min} MINUTO(S)')


if __name__ == "__main__":
    main()
