# https://www.beecrowd.com.br/judge/pt/problems/view/1847

# Bem-vindos e bem-vindas à Escola de Inverno da Maratona de Programação 2015 de Erechim! Esperamos sinceramente que vocês aprendam muito nestes dias para que tenham muito sucesso nas competições de Programação ainda por vir, mas sobretudo esperamos que vocês curtam a Escola, pois quando nos divertimos e temos prazer em estudar e programar, o treino deixa de ser um fardo e se torna um hobby. Então, divirtam-se!
# O inverno é uma estação maravilhosa, não é mesmo? Todos nós amamos vestir um poncho, participar de uma roda de chimarrão, assar pinhões no fogão a lenha… Mas nem todos gostam do inverno, especialmente em lugares onde o inverno costuma ser muito cruel. Em Westeros, por exemplo, o humor das pessoas é definido de acordo com as tendências climáticas. Com base nas temperaturas dos três últimos dias, as pessoas podem ficar tristes ou felizes, ficando mais propensas a fazer guerra ou fazer amor, respectivamente. E, sejamos sinceros, é justamente por causa das cenas de amor e de guerra que amamos Game of Thrones!

# Se a temperatura desceu do 1º para o 2º dia, mas subiu ou permaneceu constante do 2º para o 3º, as pessoas ficam felizes (primeira figura).
# Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º no mínimo o tanto que descera do 1º para o 2º, as pessoas ficam tristes (sexta figura).
# Se a temperatura desceu do 1º para o 2º dia e do 2º para o 3º, mas desceu do 2º para o 3º menos do que descera do 1º para o 2º, as pessoas ficam felizes (quinta figura).

# Se a temperatura subiu do 1º para o 2º dia, mas desceu ou permaneceu constante do 2º para o 3º, as pessoas ficam tristes (segunda figura).
# Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º menos do que subira do 1º para o 2º, as pessoas ficam tristes (terceira figura).
# Se a temperatura subiu do 1º para o 2º dia e do 2º para o 3º, mas subiu do 2º para o 3º no mínimo o tanto que subira do 1º para o 2º, as pessoas ficam felizes (quarta figura).

# Se a temperatura permaneceu constante do 1º para o 2º dia, as pessoas ficam felizes se subiu do 2º para o 3º dia ou tristes caso contrário (respectivamente, sétima e oitava figuras).

# Entrada
# A entrada consiste apenas de três inteiros, A, B e C (-100 ≤ A, B, C ≤ 100), os quais representam respectivamente as temperaturas registradas no 1º, no 2º e no 3º dias.

# Saída
# Imprima uma linha contendo uma carinha feliz ou triste, representando como fica o humor do povo de Westeros de acordo com as tendências climáticas.

def modulo(numero: int) -> int:
    return numero if numero >= 0 else -numero


def avaliar_temperaturas(temperaturas: list[int]) -> bool:
    temp1, temp2, temp3 = temperaturas

    # Temperaturas dos 2 primeiros dias iguais
    if temp1 == temp2:
        return temp3 > temp2

    # Temperatura subiu do primeiro pro segundo dia
    if temp2 > temp1:
        # Temperatura desceu ou ficou constante do segundo pro terceiro dia
        if temp3 <= temp2:
            return False
        # Temperatura subiu do segundo pro terceiro dia
        # Temperatura subiu mais do primeiro pro segundo do que do segundo pro terceiro
        if modulo(temp3 - temp2) < modulo(temp2 - temp1):
            return False
        # Temperatura subiu segundo pro terceiro mais ou igual do que do primeiro para o segundo
        if modulo(temp3 - temp2) >= modulo(temp2-temp1):
            return True

    # Temperatura desceu do primeiro pro segundo dia
    if temp2 < temp1:
        # Temperatura subiu ou ficou igual do segundo pro terceiro dia
        if temp3 >= temp2:
            return True

        # Temperatura desceu do segundo pro terceiro dia
        # Temperatura desceu mais ou ficou igual do segundo pro terceiro do que do primeiro pro segundo
        if modulo(temp3 - temp2) >= modulo(temp2 - temp1):
            return False
        # Temperatura desceu menos do segundo pro terceiro do que do primeiro pro segundo
        if modulo(temp3 - temp2) < modulo(temp2 - temp1):
            return True
    return True


def main() -> None:
    temperaturas = [int(temperatura) for temperatura in input().split()]

    if avaliar_temperaturas(temperaturas):
        print(':)')
    else:
        print(':(')


if __name__ == "__main__":
    main()
