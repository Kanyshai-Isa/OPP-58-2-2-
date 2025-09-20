#Инкапсуляция
# 1. Публичный
# 2. Защищенный. Имя атрибута начинается с одного подчеркивания (например, _balance)
# 3. Приватный. начинается с двух подчеркиваний (например, __balance)
# Инкапсуляция позволяет определить контролируемый доступ к данным,
# хранящимся внутри объектов вашего класса .
# Это позволяет писать чистый, читаемый и эффективный код и предотвращать
# случайное изменение или удаление данных класса.
#чтобы логика работала внутри класса, отделить логику, чтобы извне не пользовались
#
#
# class BankAccount():
#
#     def __init__(self, login, password, balance):
#         self.login = login
#         self._balance = balance #защищен
#         self.__password = password #приват
#
#
#     def check_balance(self, password):
#         if password == self.__password:
#             print(self._balance)  #2 тут не подчеркивалось, внутри класса можно обращаться
#         else:
#             print("Неправильный пароль!")
#
#     def __reset_def_pass(self):
#         self.password = "345"
#
#     def reset_pass(self, password):
#         if password == self.__password:
#             self.__reset_def_pass()
#         else:
#             print("Неправильный пароль!!")
#
#
#
#
#
# user_1 = BankAccount("Kanyshai", "342", "2222")

#1
# print(user_1._balance) #желтым подчеркнуто, сразу не находится, без def check_balance(self):
# print(user_1.__password) #выйдет AttributeError: 'BankAccount' object has no attribute '__password'
#когда пытаешь узнать пароль вне класса не получается


#3
# user_1.check_balance("123") #выйдет 2222

#4
# user_1.reset_pass("342") #Неправильный пароль!!
#
# print(user_1._BankAccount__password)
#
# print(dir(user_1))




# Абстракция позволяет сосредоточиться на общих характеристиках, скрывая детали
# реализации. Это можно сделать создавая абстактные классы, которые определяют
# интерфейс (методы) для классов наследников. В питоне абстрактные классы обычно
# создаются с помощью модуля abc


# from abc import ABC, abstractmethod
#
# #Абстрактный класс
# class Animal(ABC):
#
# #указываем что должны в точности реализовать дочерние классы
#     @abstractmethod
#     def make_sound(self):
#         pass
#
#     @abstractmethod
#     def move(self):
#         pass
#
# class Dog(Animal):
#
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print(f'{self.name} gaf gaf')
#
# #выходит ошибка если не реализован все методы указанные вверху. например без move
#     def move(self):
#         print(f'{self.name} step')
#
#
# gufi = Dog('Gufi')
#
#
# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         print(f'{self.name} myau myau')
#
#     def move(self):
#         print(f'{self.name} step')




#пример отправки смс в разные страны. должен реализоваться метод,
# но в разных странах он свой

from abc import ABC, abstractmethod
class SendSms(ABC):

    @abstractmethod
    def send_otp(self):
        pass

class KRSendSms(SendSms):

    def send_otp(self):
        print(f'Отправил смс в КР')
        msg = f"<text>123321<text/><phone>+99679<phone/>"

class RSSendSms(SendSms):
    def send_otp(self):
        msg = {
            "text": "text",
            "phone": "+99679"
        }