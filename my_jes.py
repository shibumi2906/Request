import requests

# URL API GitHub для поиска репозиториев
url = "https://api.github.com/search/repositories"

# Параметры запроса
params = {
    "q": "language:html"  # Поиск репозиториев, где основной язык - HTML
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Печатаем статус-код ответа
print("Статус-код:", response.status_code)

# Печатаем содержимое ответа в формате JSON
print("Ответ в формате JSON:")
print(response.json())
