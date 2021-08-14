# https://www.urionlinejudge.com.br/judge/pt/problems/view/1117

# Faça um programa que leia as notas referentes às duas avaliações de um aluno. Calcule e imprima a média semestral. Faça com que o algoritmo só aceite notas válidas (uma nota válida deve pertencer ao intervalo [0,10]). Cada nota deve ser validada separadamente.

# Entrada
# A entrada contém vários valores reais, positivos ou negativos. O programa deve ser encerrado quando forem lidas duas notas válidas.

# Saída
# Se uma nota inválida  for lida, deve ser impressa a mensagem "nota invalida".
# Quando duas notas válidas forem lidas, deve ser impressa a mensagem "media = " seguido do valor do cálculo. O valor deve ser apresentado com duas casas após o ponto decimal.

def main() -> None:

    validas = 0
    soma: float = 0.0
    while True:
        if validas == 2:
            break
        nota = float(input())
        if 0 <= nota <= 10:
            validas += 1
            soma += nota
        else:
            print('nota invalida')
    media: float = soma / 2
    print('media = {}' .format(media))


if __name__ == "__main__":
    main()
