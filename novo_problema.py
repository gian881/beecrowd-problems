from typing import TextIO
import cloudscraper
import bs4
from bs4 import BeautifulSoup
from unidecode import unidecode
import sys
import datetime


def add_log(message: str):
    tempo_agora = datetime.datetime.now()
    print(f'[{tempo_agora.strftime("%H:%M:%S")}] - {message}')


def write_paragrafo(file: TextIO, textos: list[str]):
    for text in textos:
        if '\n' in text:
            paragrafos = [paragrafo.strip() for paragrafo in text.split('\n')]
            for paragrafo in paragrafos:
                if paragrafo == '':
                    file.write('\n')
                else:
                    file.write(f'# {paragrafo}\n')
        else:
            file.write(f'# {text}\n')


class Problema:
    titulo: str
    descricao: list[str]
    entrada: list[str]
    saida: list[str]
    soup: BeautifulSoup

    def __init__(self, problem_number) -> None:
        add_log('Fazendo request.')
        scraper: cloudscraper.CloudScraper = cloudscraper.create_scraper()
        self.soup = BeautifulSoup(scraper.get(
            f'https://www.beecrowd.com.br/repository/UOJ_{problem_number}.html').content, 'html.parser')
        self.titulo = self.get_titulo()
        self.descricao = self.get_lista_de_paragrafos('description')
        self.entrada = self.get_lista_de_paragrafos('input')
        self.saida = self.get_lista_de_paragrafos('output')
        self.number = problem_number
        print(self.soup)

    def get_titulo(self) -> str:
        title: str = self.soup.find('h1').get_text().replace(
            '!', ' ').replace('?', ' ').replace('.', '').replace(',', '').strip()
        return unidecode(title)

    def get_lista_de_paragrafos(self, classe: str) -> list[str]:
        paragrafos_tag = self.soup.find('div', {'class': classe})
        paragrafos: list[str] = []

        if paragrafos_tag is not None:
            for tag in paragrafos_tag:
                if isinstance(tag, bs4.element.Tag):
                    if tag.find('img'):
                        paragrafos.append(tag.find('img')['src'].strip())
                    elif tag.get_text().strip() != '':
                        paragrafos.append(tag.get_text().strip())

        return paragrafos

    def write_end_of_file(self, file: TextIO) -> None:
        file.write('\n\n')
        file.write('if __name__ == "__main__":\n')
        file.write('    main()\n')

    def write_descricao(self, file: TextIO) -> None:
        file.write(
            f'# https://www.beecrowd.com.br/judge/pt/problems/view/{self.number}\n\n')
        write_paragrafo(file, self.descricao)
        file.write('\n')
        file.write('# Entrada\n')
        write_paragrafo(file, self.entrada)
        file.write('\n')
        file.write('# Saída\n')
        write_paragrafo(file, self.saida)
        file.write('\n')
        file.write('def main() -> None:\n')

    def criar_arquivo(self):
        add_log(f'Criando novo arquivo com o problema {self.number}.')
        with open(f'{self.number}-{self.titulo}.py'.replace(' ', '_'), 'w', encoding='utf-8') as file:
            self.write_descricao(file)
            file.write('    pass')
            self.write_end_of_file(file)

    def atualizar_arquivo(self):
        add_log(
            f'Atualizando arquivo de problema já criado {self.number}.')
        with open(f'.\\Aceitos\\{self.number}-{self.titulo}.py'.replace(' ', '_'), 'r', encoding='utf-8') as file:
            linhas: list[str] = [
                f'    {linha}' for linha in file if not linha.startswith("#")]

        with open(f'.\\Aceitos\\{self.number}-{self.titulo}.py'.replace(' ', '_'), 'w', encoding='utf-8') as file:
            self.write_descricao(file)
            for linha in linhas:
                file.write(linha)
            self.write_end_of_file(file)


def main() -> None:
    problem_number: str
    ja_existe: bool

    try:
        if len(sys.argv) == 3:
            problem_number, ja_existe = sys.argv[1], sys.argv[2] == 's'
        else:
            problem_number, ja_existe = sys.argv[1], False
    except IndexError:
        lista: list[str] = input(
            'Digite o número do problema e se já existe: ').strip().split()
        if len(lista) == 2:
            problem_number, ja_existe = lista[0], lista[1] == 's'
        else:
            problem_number, ja_existe = lista[0], False

    problema = Problema(problem_number)

    if ja_existe:
        problema.atualizar_arquivo()
    else:
        problema.criar_arquivo()


if __name__ == "__main__":
    main()
