#Отправить запрос для получения всех категорий

import requests

class TestCreateJoke():
    """Класс включающий сценарии по отправке запросов, с целью получения шуток с Чаком Норрисом"""

    def test_create_randome_joke_category_positive(self):
        url = 'https://api.chucknorris.io/jokes' #прописываем основной url
        category = '/categories' #конкретизируем эндпоинт для получения списка категорий
        category_url = url+category #склеиваем uri для получения списка категорий
        category_response = requests.get(category_url) #осуществляем GET-метод
        category_values=category_response.json() #преобразуем в json формат
        for i in category_values:  #запускаем цикл по списку категорий
            joke_url = url + f'/random?category={i}'  #склеиваем uri и подтавляем по  очереди категории из списка
            joke_response = requests.get(joke_url) #осуществляем GET-метод
            values = joke_response.json() #преобразуем в json формат
            #print(values)
            print(f'Статус-код: {joke_response.status_code}')
            assert joke_response.status_code == 200, 'Ошибка статус кода'
            print('Статус-код корректен')
            print(values)
        print("Тест прошел успешно")

start = TestCreateJoke().test_create_randome_joke_category_positive()