# https://www.beecrowd.com.br/judge/pt/problems/view/1049

# Neste problema, você deverá ler 3 palavras que definem o tipo de animal possível segundo o esquema abaixo, da esquerda para a direita.  Em seguida conclua qual dos animais seguintes foi escolhido, através das três palavras fornecidas.
# https://resources.urionlinejudge.com.br/gallery/images/problems/UOJ_1049_b.png

# Entrada
# A entrada contém 3 palavras, uma em cada linha, necessárias para identificar o animal segundo a figura acima, com todas as letras minúsculas.

# Saída
# Imprima o nome do animal correspondente à entrada fornecida.

def main() -> None:

    a = input()
    b = input()
    c = input()

    if a == 'vertebrado':
        if b == 'ave':
            if c == 'carnivoro':
                print('aguia')
            elif c == 'onivoro':
                print('pomba')
        elif b == 'mamifero':
            if c == 'onivoro':
                print('homem')
            elif c == 'herbivoro':
                print('vaca')
    elif a == 'invertebrado':
        if b == 'inseto':
            if c == 'hematofago':
                print('pulga')
            elif c == 'herbivoro':
                print('lagarta')
        elif b == 'anelideo':
            if c == 'hematofago':
                print('sanguessuga')
            elif c == 'onivoro':
                print('minhoca')


if __name__ == "__main__":
    main()
