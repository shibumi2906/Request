import requests

# URL для API, который мы будем использовать для отправки POST-запроса
url = "https://jsonplaceholder.typicode.com/posts"

# Создаем словарь с данными для отправки
data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос
response = requests.post(url, json=data)

# Печатаем статус-код ответа
print("Статус-код:", response.status_code)

# Печатаем содержимое ответа в формате JSON
print("Ответ в формате JSON:")
print(response.json())
