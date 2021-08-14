# https://www.urionlinejudge.com.br/judge/pt/problems/view/1015

# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1015.png

# Entrada
# O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

# Saída
# Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.

def main() -> None:

    valores1 = input().strip().split()
    valores2 = input().strip().split()

    x1 = float(valores1[0])
    y1 = float(valores1[1])
    x2 = float(valores2[0])
    y2 = float(valores2[1])

    d = ((x2 - x1)**2 + (y2 - y1)**2)
    d = (d)**0.5

    print('{:.4f}' .format(d))


if __name__ == "__main__":
    main()
