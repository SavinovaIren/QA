"""Создайте класс Car. Добавьте обязательные атрибуты класса:
модель, год выпуска, объем двигателя, цена, пробег, количество колес = 4.
Создайте 1 экземпляр класса
Создать класс наследник - Грузовик. Который, наследует все атрибуты класса, но количество колес = 8.
Создать 1 экземпляр класса Наследника
Добавить метод, который возвращает информацию по объекту (как в учебном видео метод description)"""

class Car:
    def __init__(self, model, year, value, mileage, price):
        self.model = model
        self.year = year
        self.value = value
        self.mileage = mileage
        self.price = price
        self.wheels = 4

    def description(self):
        """Получение описания алфавита"""
        description = (f"Модель - {self.model}, год выпуска - {self.year}, "
                       f"объем двигателя - {self.value}, цена - {self.price},  пробег - {self.mileage},"
                       f"количество колес - {self.wheels}")

        print(description)

class Truck(Car):
    def __init__(self, model, year, value, mileage, price):
        super().__init__(model, year, value, mileage, price)
        self.wheels = 8

car = Car('модель', '2005', 'объем', '12333',
    '76688p')

car.description()
truck = Truck('модель1', '2012', 'объем', '125333',
    '8876688p')
truck.description()





