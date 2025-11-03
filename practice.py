from abc import ABC, abstractmethod

# 1 Оплата
class Payment(ABC):
    @abstractmethod
    def pay(self, amount): pass
    @abstractmethod
    def refund(self, amount): pass

class CreditCardPayment(Payment):
    def pay(self, amount): print(f"Оплата {amount} сом по кредитной карте")
    def refund(self, amount): print(f"Возврат {amount} сом на кредитную карту")

class CryptoPayment(Payment):
    def pay(self, amount): print(f"Оплата {amount} сом в криптовалюте")
    def refund(self, amount): print(f"Возврат {amount} сом в криптовалюте")

payments = [CreditCardPayment(), CryptoPayment()]
for p in payments:
    p.pay(500)
    p.refund(200)

# 2 Курсы
class Course(ABC):
    @abstractmethod
    def start(self): pass
    @abstractmethod
    def get_materials(self): pass
    @abstractmethod
    def end(self): pass

class PythonCourse(Course):
    def start(self): print("Курс Python начинается!")
    def get_materials(self): print("Материалы: Python, переменные, циклы")
    def end(self): print("Курс Python завершён!")

class MathCourse(Course):
    def start(self): print("Курс Математика начинается!")
    def get_materials(self): print("Материалы: алгебра, геометрия, тригонометрия")
    def end(self): print("Курс Математика завершён!")

courses = [PythonCourse(), MathCourse()]
for c in courses:
    c.start()
    c.get_materials()
    c.end()

# 3 Доставка
class Delivery(ABC):
    @abstractmethod
    def calculate_cost(self, distance): pass
    @abstractmethod
    def deliver(self): pass

class AirDelivery(Delivery):
    def calculate_cost(self, distance): return distance * 10
    def deliver(self): print("Доставка самолётом выполнена")

class GroundDelivery(Delivery):
    def calculate_cost(self, distance): return distance * 5
    def deliver(self): print("Доставка наземным транспортом выполнена")

class SeaDelivery(Delivery):
    def calculate_cost(self, distance): return distance * 2
    def deliver(self): print("Доставка морем выполнена")

deliveries = [AirDelivery(), GroundDelivery(), SeaDelivery()]
for d in deliveries:
    print(f"Стоимость: {d.calculate_cost(100)} сом")
    d.deliver()

# 4 Банковский счёт
class BankAccount:
    def __init__(self, owner, pin):
        self.__owner = owner
        self.__balance = 0
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin == self.__pin and amount > 0:
            self.__balance += amount
            print(f"Внесено {amount}, баланс {self.__balance}")
        else:
            print("Ошибка депозита или PIN")

    def withdraw(self, amount, pin):
        if pin == self.__pin and 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Снято {amount}, баланс {self.__balance}")
        else:
            print("Ошибка снятия или PIN")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN изменён")
        else:
            print("Неверный старый PIN")

account = BankAccount("Сулайман", 1234)
account.deposit(1000, 1234)
account.withdraw(500, 1234)
account.change_pin(1234, 4321)

# 5 Профиль пользователя
class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self._status = "regular"

    def login(self, email, password):
        if self.__email == email and self.__password == password:
            print("Вход выполнен")
        else:
            print("Неверный логин или пароль")

    def upgrade_to_premium(self):
        self._status = "premium"
        print("Статус обновлён до premium")

    def get_info(self):
        print(f"Email: {self.__email}, Статус: {self._status}")

user = UserProfile("email@mail.com", "12345")
user.login("email@mail.com", "12345")
user.upgrade_to_premium()
user.get_info()

# 6 Товар
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0

    def get_price(self):
        return self.price * (1 - self.__discount)

    def set_discount(self, discount, is_admin=False):
        if is_admin:
            self.__discount = discount
            print(f"Скидка {discount*100}% установлена")
        else:
            print("Нет прав для скидки")

product = Product("Ноутбук", 50000)
print("Цена:", product.get_price())
product.set_discount(0.1, is_admin=True)
print("Цена со скидкой:", product.get_price())

# 7 Файлы
class TextFile:
    def open(self): print("Открыт текстовый файл")
class ImageFile:
    def open(self): print("Открыт изображение файл")
class AudioFile:
    def open(self): print("Открыт аудио файл")

def open_all(files):
    for f in files:
        f.open()

files = [TextFile(), ImageFile(), AudioFile()]
open_all(files)

# 8 Транспорт
class Car:
    def move(self, distance): print(f"Машина проехала {distance} км за {distance/60:.1f} ч")
class Truck:
    def move(self, distance): print(f"Грузовик проехал {distance} км за {distance/40:.1f} ч")
class Bicycle:
    def move(self, distance): print(f"Велосипед проехал {distance} км за {distance/15:.1f} ч")

transports = [Car(), Truck(), Bicycle()]
for t in transports:
    t.move(30)

# 9 Доступ к порталу
class Student:
    def access_portal(self): print("Студент видит расписание")
class Teacher:
    def access_portal(self): print("Преподаватель выставляет оценки")
class Administrator:
    def access_portal(self): print("Админ управляет пользователями")

users = [Student(), Teacher(), Administrator()]
for u in users:
    u.access_portal()
