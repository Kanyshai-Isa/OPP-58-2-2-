#проблемы наследования
#VENV
#
# class Fly:
#     def fly(self):
#         print('Fly')
#
# class Swim:
#     def swim(self):
#         print('Swim')
#
# #наследует от 2х классов
# class Duck(Fly, Swim):
#     pass
#
# donald_duck = Duck()
# donald_duck.fly()
# donald_duck.swim()




#у наследования есть минусы(например методы с одинаковыми названиями):

# class Fly:
#     def action(self):
#         print('Fly')
#
# class Swim:
#     def action(self):
#         print('Swim')
#
# #наследует от 2х классов
# class Duck(Fly, Swim):
#     pass
#
# donald_duck = Duck()
# donald_duck.action()  #Fly  так как по списку наследования первым Fly, идет к родительскому
# donald_duck.action()  #Fly




#ромбовидно: a - bc - d алмазная проблема
# class A:
#     def action(self):
#         print('A')
#
# class B(A):
#     def action(self):
#         print('B')
#
# class C(A):
#     def action(self):
#         print('C')
#
# class D(B, C):
#     def action(self):
#         print('D')
#
# obj = D()
# obj.action()   #D


#если в D pass сделаем
# class A:
#     def action(self):
#         print('A')
#
# class B(A):
#     def action(self):
#         print('B')
#
# class C(A):
#     def action(self):
#         print('C')
#
# class D(B, C):
#     pass
#
# obj = D()
# obj.action()   #B

#
# class A:
#     def action(self):
#         print('A')
#
# class B(A):
#     def action(self):
#         super().action()  #ссылка на родительский класс
#         print('B')
#
# class C(A):
#     def action(self):
#         print('C')
#
# class D(B, C):
#     pass
#
# obj = D()
# obj_2 = B()
# obj.action()   #C B
# obj_2.action() #A B
# print(D.__mro__) #порядок выполнения
#(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
#Method Resolution Order


#модули - все файлы которые с .py
#директории с несколькими модулями становится пакетом
#конструктор пакета __init__.py
#создали пакет  - my_package
#пустые проблемы не оставлять в наименованиях и кириллица запрещена
#создали module_1, main, туда сюда попередавали данные
#создали module_2
#можно использовать внешние
# открываем терминал ,в начале должно быть написано venv, если нет то .venv\Scripts\activate
#pip install colorama
# print("some text")

# from colorama import *

#склонировали чужой проект
#py -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt #чтобы прочитал все построчно в файле и скачал
#запускаем проект