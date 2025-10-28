"""1.Запросить у пользователя категорию, на которую он хочет получить шутку (не сами сохранить в переменную, а через input() и ввести в терминале
2.Отправить запрос для получения всех категорий
3.убедиться что данная категория (из пункта 1) есть в ответе запроса (отправленного в пункте 2)
4.Отправить запрос для получения шутки, которую запросил пользователь
5.Добавить в код комментарии, аннотации, print, проверки на статус код для лучшей читаемости кода"""
import requests
"""class TestCreateJoke():

    def test_create_input_joke_category(self):
        url = 'https://api.chucknorris.io/jokes'
        category = '/categories'  # конкретизируем эндпоинт для получения списка категорий
        category_url = url+category
        category_response = requests.get(category_url)
        print(category_response.json())
        input_joke = input()
        user_url = url + f'/random?category={input_joke}'
        user_response = requests.get(user_url)
        user_value = user_response.json()
        if user_value in category_response:
            print(user_value)
        else:
            print('Такой категории нет')

        joke_category = check_joke.get("categories")
        print(joke_category)
        assert joke_category[0] == category, 'ОШИБКА, Статус-код не совпадает'
        print('Категория корректна')

start = TestCreateJoke().test_create_input_joke_category()"""
import requests
class TestCreateJoke():

    def test_create_input_joke_category(self):
        url = 'https://api.chucknorris.io/jokes'
        category = '/categories'  # конкретизируем эндпоинт для получения списка категорий
        category_url = url+category #Собираем uri с эндпойтом для получения категорий
        category_response = requests.get(category_url) #осуществляем GET-метод
        categories = category_response.json() #Список категорий преобразуем в json
        print("Доступные категории:",categories)

        input_category = input("Введите категорию:") #Запрашиваем категорию у пользователя
        try: #Делаем проверку на наличие категории
            assert input_category in categories, 'Такой категории нет'
        except AssertionError as e:
            print(e)
            return  # завершить выполнение или обработать иначе

        user_url = url + f'/random?category={input_category}' #Собираем uri с категорией пользователя
        user_response = requests.get(user_url) #осуществляем GET-метод
        user_value = user_response.json() #Список категорий преобразуем в json
        print(f'Шутка из категории \'{input_category}\' - '+ user_value['value'])


start = TestCreateJoke().test_create_input_joke_category()