# https://www.beecrowd.com.br/judge/pt/problems/view/1134

# Um Posto de combustíveis deseja determinar qual de seus produtos tem a
# preferência de seus clientes. Escreva um algoritmo para ler o tipo de
# combustível abastecido (codificado da seguinte forma: 1.Álcool
# 2.Gasolina 3.Diesel 4.Fim). Caso o usuário informe um código inválido
# (fora da faixa de 1 a 4) deve ser solicitado um novo código (até que
# seja válido). O programa será encerrado quando o código informado for o
# número 4.

# Entrada
# A entrada contém apenas valores inteiros e positivos.

# Saída
# Deve ser escrito a mensagem: "MUITO OBRIGADO" e a quantidade de
# clientes que abasteceram cada tipo de combustível, conforme exemplo.

def main() -> None:

    alcool = gasolina = diesel = 0
    lista = [1, 2, 3, 4]

    while True:
        resposta = 0
        while resposta not in lista:
            resposta = int(input())
        if resposta == 1:
            alcool += 1
        elif resposta == 2:
            gasolina += 1
        elif resposta == 3:
            diesel += 1
        else:
            break

    print('MUITO OBRIGADO')
    print('Alcool: {}' .format(alcool))
    print('Gasolina: {}' .format(gasolina))
    print('Diesel: {}' .format(diesel))


if __name__ == "__main__":
    main()
