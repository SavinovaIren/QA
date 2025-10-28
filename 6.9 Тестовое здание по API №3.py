"""1. Отправить метод POST

2. Создать текстовый файл в котором хранить 5 шт place_id полученных из 1 пункта (не писать портянку вызывая 5 раз метод, сделать красиво)

3. Отправить метод Get который будет читать place_id из текстового файла (из него, не из переменной первого запроса) и убедиться что данные place_id существуют
"""

import requests
class TestNewLocation():

    def test_create_new_lication(self):

        url = 'https://rahulshettyacademy.com' #прописываем основной url
        post_end = '/maps/api/place/add/json' #конкретизируем эндпоинт для post метода
        key = '?key=qaclick123'
        post_url = url + post_end + key #склеиваем uri
        #тело запроса
        json_body = {
                    "location": {
                        "lat": -38.383494,
                        "lng": 33.427362
                    },
                    "accuracy": 50,
                    "name": "Frontline house",
                    "phone_number": "(+91) 983 893 3937",
                    "address": "29, side layout, cohen 09",
                    "types": [
                        "shoe park",
                        "shop"
                    ],
                    "website": "http://google.com",
                    "language": "French-IN"
                    }
        print('-' * 220+ '\n' + 'Запись place id в файл location.txt' + '\n' + '-' * 220)
        for i in range(5):  #цикл для создания 5 записей в location.txt
            post_result = requests.post(url=post_url, json=json_body)
            result = post_result.json()
            print(f'Статус-код теста №{i+1}: {post_result.status_code}')
            assert post_result.status_code == 200, 'ОШИБКА, Статус-код не совпадают'
            print(f'Статус-код POST теста №{i+1} корректен')
            print(f"В файл записано значение place id: {result['place_id']}")
            print('-' * 220)
            with open('location.txt', 'a') as file:  # создание файла location.txt для записи значений
                file.write(result['place_id'] + '\n')  #запись значений в файл

        get_end = '/maps/api/place/get/json' # конкретизируем эндпоинт для get метода

        print('-' * 220+ '\n' + 'Чтение координат по place id из файла location.txt' + '\n' + '-' * 220)

        with open('location.txt', 'r') as file: # открытие файла location.txt для чтения значений
            lines = file.readlines()
            for i in range(len(lines)):  # запуск цикла для поочередного вывода строки из файла location.txt
                place_id = lines[i].strip() #удаление лишний символов в строке
                get_url = url + get_end + key + '&place_id=' + place_id #склеиваем uri
                print(f'Запрос GET по адресу: {get_url}')
                get_result = requests.get(get_url) # формирование запроса с методом GET
                print(f'Статус-код теста № {i+1}: {get_result.status_code}')
                assert get_result.status_code == 200, "ОШИБКА, Статус-код не совпадают"
                print(f'Статус-код GET теста № {i+1} корректен')
                print(f'Результат: {get_result.json()}')
                print('-'*220)

test=TestNewLocation().test_create_new_lication()