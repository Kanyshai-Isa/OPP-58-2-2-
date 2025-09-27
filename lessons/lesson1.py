class Hero:
# Класс пишется: верблюжья нотация HeroMag

    #конструктор класса
    def __init__(self, name, lvl, hp):
        #атрибуты класса (например, имя, номер телефона и тд)
        self.name = name  #ссылка на объект класса, тут self=kirito
        # ниже мы обращаемся к name1 например self.name1 = name
        self.lvl = lvl  #с двух сторон должно быть имя одинаково
        self.hp = hp
#метод класса (похожи на функции, лечение защита например)
    def action(self):
        print("Base action")


#объект / экземпляр класса
#они сохраняются в атрибуты
# Объект пишется: Змеинная нотация hero_kirita
kirito = Hero("Kirito", 100, 1000)
asuna = Hero ("Asuna", 100, 1000)


text1= "text1"
text2 = "text2"

# print(text1)
# print(text2)  #это тоже самое что и ниже
# print(kirito.name)   #Kirito
# print(kirito.lvl)    #100
# print(kirito.hp)     #1000
# kirito.action()      #Base action
# print(asuna.name)      #Asuna

#
# print(type("str"))    #<class 'str'>
# print(type(123))      # <class 'int'>
# print(type(45.4))     # <class 'float'>
# print(type([True]))   # <class 'list'>
# print(type({}))       # <class 'dict'>
# print(type(()))       # <class 'tuple'>



# test = "sqvfgb"
#ctrl+
# test.   #чтобы узнать методы


# test = []
# test.remove(kirito)
#выходят другие методы

# kirito.action()
#у нашего объекта также есть методы

import random