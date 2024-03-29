# https://www.beecrowd.com.br/judge/pt/problems/view/1020

# Leia um valor inteiro correspondente à idade de uma pessoa em dias e informe-a em anos, meses e dias
# Obs.: apenas para facilitar o cálculo, considere todo ano com 365 dias e todo mês com 30 dias. Nos casos de teste nunca haverá uma situação que permite 12 meses e alguns dias, como 360, 363 ou 364. Este é apenas um exercício com objetivo de testar raciocínio matemático simples.

# Entrada
# O arquivo de entrada contém um valor inteiro.

# Saída
# Imprima a saída conforme exemplo fornecido.

def main() -> None:
    dias = int(input())
    anos = dias // 365
    dias %= 365
    meses = dias // 30
    dias %= 30
    print('{} ano(s)' .format(anos))
    print('{} mes(es)' .format(meses))
    print('{} dia(s)' .format(dias))


if __name__ == "__main__":
    main()
