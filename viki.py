import requests
from bs4 import BeautifulSoup
import time

# Константы для работы с Википедией
WIKI_URL = "https://ru.wikipedia.org/w/index.php"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def get_wiki_page(search_query):
    """ Получает страницу Википедии по заданному поисковому запросу """
    try:
        params = {'search': search_query}
        response = requests.get(WIKI_URL, headers=HEADERS, params=params)
        return response.text
    except requests.RequestException as e:
        return "Ошибка при запросе к Википедии: " + str(e)

def parse_wiki_page(html_content):
    """ Разбирает HTML-содержимое страницы Википедии и извлекает первый параграф и ссылки """
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        content = soup.find('div', {'class': 'mw-parser-output'})
        paragraphs = content.find_all('p', recursive=False)
        first_paragraph = paragraphs[0].text if paragraphs else "Содержание отсутствует."
        links = []
        for link in content.find_all('a', recursive=False):
            if link.get('href', '').startswith('/wiki/'):
                links.append((link.text, "https://ru.wikipedia.org" + link['href']))
        return first_paragraph, links[:5]
    except Exception as e:
        return "Ошибка при анализе страницы: " + str(e), []

def interactive_wiki_search():
    """ Управляет интерактивным поиском и навигацией по Википедии """
    try:
        last_visited = None
        search_query = input("Введите запрос для поиска на Википедии: ")
        html_content = get_wiki_page(search_query)
        if "Ошибка" in html_content:
            print(html_content)
            return
        first_paragraph, links = parse_wiki_page(html_content)
        last_visited = first_paragraph

        while True:
            print("\nПервый параграф статьи:\n", first_paragraph)
            print("\nСвязанные страницы:")
            for i, (title, url) in enumerate(links):
                print(f"{i+1}. {title} - {url}")

            choice = input("\nВыберите опцию (1-Читать дальше, 2-Перейти на связанную страницу, 3-Выход): ")
            time.sleep(5)

            if choice == '1':
                continue
            elif choice == '2':
                link_number = int(input("Введите номер страницы для перехода: "))
                html_content = get_wiki_page(links[link_number-1][0])
                first_paragraph, links = parse_wiki_page(html_content)
                last_visited = first_paragraph
            elif choice == '3':
                print("Выход из программы.")
                print("Последний просмотренный текст:\n", last_visited)
                break
            else:
                print("Неверный ввод. Попробуйте снова.")
    except Exception as e:
        print("Произошла ошибка: ", str(e))

interactive_wiki_search()


