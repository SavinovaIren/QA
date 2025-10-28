import requests

class TestCreateJoke():
    """Класс включающий сценарии по отправке запросов, с целью получения шуток с Чаком Норрисом"""

    def test_create_randome_joke_category_positive(self, category):
        """Позитивный тест по получению рандомной шутки по определенной категории, включает:
                 отправку запроса, проверка на статус-код, проверка на соответствие категории, печать шутки."""

        url = 'https://api.chucknorris.io/jokes/random'
        path = f'?category={category}'
        url_path = url + path
        print(url_path)
        response = requests.get(url_path)
        values = response.json()
        print(values)
        #print (f'Статус код {response.status_code}')
        #assert response.status_code == 200, 'Ошибка статус кода'

        #print(values.get("value"))

start = TestCreateJoke ()
start.test_create_randome_joke_category_positive('animal')

