# 1 Работа

class Account:
    def __init__(self, number, balance, pin):
        self.__number = number
        self.__balance = balance
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin == self.__pin:
            self.__balance += amount

    def withdraw(self, amount, pin):
        if pin == self.__pin and amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self, pin):
        if pin == self.__pin:
            return self.__balance


class Product:
    def __init__(self, price):
        self.__price = price

    def set_discount(self, percent):
        self.__price = max(0, self.__price - self.__price * percent / 100)

    def final_price(self):
        return self.__price


# 2 Работа

class Course:
    def __init__(self, name, max_students):
        self.__name = name
        self.__students = []
        self.__max_students = max_students

    def add_student(self, name):
        if len(self.__students) < self.__max_students:
            self.__students.append(name)

    def remove_student(self, name):
        if name in self.__students:
            self.__students.remove(name)

    def get_students(self):
        return self.__students[:]


# 3 Работа

class SmartWatch:
    def __init__(self, battery):
        self.__battery = battery

    def use(self, minutes):
        self.__battery -= minutes / 10
        if self.__battery < 0:
            self.__battery = 0

    def charge(self, percent):
        self.__battery += percent
        if self.__battery > 100:
            self.__battery = 100

    def get_battery(self):
        return self.__battery


# 4 Работа

class Transport:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def travel_time(self, distance):
        return distance / self.speed

class Bus(Transport):
    pass

class Train(Transport):
    pass

class Airplane(Transport):
    def travel_time(self, distance):
        return super().travel_time(distance) * 0.8


# 5 Работа

class Order:
    def __init__(self, amount):
        self.amount = amount

    def calculate_total(self):
        return self.amount

class DineInOrder(Order):
    def calculate_total(self):
        return self.amount * 1.1

class TakeAwayOrder(Order):
    def calculate_total(self):
        return self.amount * 1.05

class DeliveryOrder(Order):
    def calculate_total(self):
        return self.amount * 1.15


# 6 Работа

class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack_power = attack

    def attack(self):
        return 0

class Warrior(Character):
    def attack(self):
        return f"{self.name} атакует мечом на {self.attack_power}"

class Mage(Character):
    def attack(self):
        return f"{self.name} атакует магией на {self.attack_power}"

class Archer(Character):
    def attack(self):
        return f"{self.name} атакует луком на {self.attack_power}"


# 7 Работа

class MediaFile:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def play(self):
        pass

class AudioFile(MediaFile):
    def play(self):
        return f"Воспроизводится аудио: {self.name}"

class VideoFile(MediaFile):
    def play(self):
        return f"Воспроизводится с изображением: {self.name}"

class Podcast(MediaFile):
    def play(self):
        return f"Воспроизводится эпизод: {self.name}"


# 8 Работа

class PaymentSystem:
    def process_payment(self, amount):
        pass

class CreditCardPayment(PaymentSystem):
    def process_payment(self, amount):
        return f"Оплачено картой: {amount}"

class CryptoPayment(PaymentSystem):
    def process_payment(self, amount):
        return f"Оплачено криптой: {amount}"

class BankTransfer(PaymentSystem):
    def process_payment(self, amount):
        return f"Оплачено через банк: {amount}"


# 9 Работа

class Animal:
    def eat(self):
        pass

    def sleep(self):
        pass

class Lion(Animal):
    def eat(self):
        return "Лев ест мясо"
    def sleep(self):
        return "Лев спит"

class Elephant(Animal):
    def eat(self):
        return "Слон ест растения"
    def sleep(self):
        return "Слон спит стоя"

class Snake(Animal):
    def eat(self):
        return "Змея ест мелких животных"
    def sleep(self):
        return "Змея спит свернувшись"


# 10 Работа

class Document:
    def open(self):
        pass
    def edit(self):
        pass
    def save(self):
        pass

class WordDocument(Document):
    def open(self):
        return "Открыт Word документ"
    def edit(self):
        return "Редактируется Word документ"
    def save(self):
        return "Сохранён Word документ"

class PdfDocument(Document):
    def open(self):
        return "Открыт PDF документ"
    def edit(self):
        return "PDF нельзя редактировать"
    def save(self):
        return "PDF сохранён"

class SpreadsheetDocument(Document):
    def open(self):
        return "Открыта таблица"
    def edit(self):
        return "Редактируется таблица"
    def save(self):
        return "Таблица сохранена"


# 11 Работа

class Lesson:
    def start(self):
        pass

class VideoLesson(Lesson):
    def start(self):
        return "Начало видео урока"

class QuizLesson(Lesson):
    def start(self):
        return "Начало теста"

class TextLesson(Lesson):
    def start(self):
        return "Начало текстового урока"


# 12 Работа

class EmailNotification:
    def send(self, message):
        return f"Email: {message}"

class SMSNotification:
    def send(self, message):
        return f"SMS: {message}"

class PushNotification:
    def send(self, message):
        return f"Push: {message}"


# 13 Работа

class Square:
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return self.side * 4

class Circle:
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def perimeter(self):
        return self.a + self.b + self.c


# 14 Работа

class Manager:
    def work(self):
        return "Менеджер управляет"

class Developer:
    def work(self):
        return "Разработчик пишет код"

class Designer:
    def work(self):
        return "Дизайнер рисует"


# 15 Работа

class FireSpell:
    def cast(self, target):
        return f"Наносит урон огнём по {target}"

class IceSpell:
    def cast(self, target):
        return f"Замораживает {target}"

class HealingSpell:
    def cast(self, target):
        return f"Восстанавливает здоровье {target}"
