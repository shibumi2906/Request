import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Создание объекта переводчика
translator = Translator()


# Функция для перевода текста с английского на русский
def translate_to_russian(text):
    # Возвращаем переведенный текст
    return translator.translate(text, src='en', dest='ru').text


# Функция, получающая английские слова и их описания с сайта
def get_english_words():
    url = "https://randomword.com/"
    try:
        # Запрос к сайту для получения случайного слова
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        # Извлечение слова
        english_word = soup.find("div", id="random_word").text.strip()
        # Извлечение определения слова
        word_definition = soup.find("div", id="random_word_definition").text.strip()

        # Перевод слова и его определения на русский язык
        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(word_definition)

        return {
            "english_word": english_word,  # оригинальное слово на английском
            "russian_word": russian_word,  # переведенное слово на русский
            "russian_definition": russian_definition  # перевод определения
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")


# Основная функция игры
def word_game():
    print("Добро пожаловать в игру")
    while True:
        # Получение данных о слове
        word_dict = get_english_words()
        russian_word = word_dict.get("russian_word")
        russian_definition = word_dict.get("russian_definition")

        # Представление определения игроку
        print(f"Значение слова - {russian_definition}")
        user = input("Что это за слово? ")
        # Проверка ответа игрока
        if user.lower() == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный, было загадано это слово - {russian_word}")

        # Запрос на продолжение игры
        play_again = input("Хотите сыграть еще раз? (y/n) ")
        if play_again.lower() != "y":
            print("Спасибо за игру!")
            break


# Запуск игры
word_game()
