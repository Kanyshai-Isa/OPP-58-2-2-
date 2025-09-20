#импорты пишем в начале

# 1. импортируем с module_1 (явный импорт)
# from module_1 import add
# print(add(1,2))

# 2. импортируем переменную с module_1
# from module_1 import add, test
# print(test) #123

# 3.импортируем все, но через module.
# import module_1
# print(module_1.add(3,4))  #7
# print(module_1.test)   #123

# 4.импортируем все "*". Но так нельзя делать
# from module_1 import *
# print(add(3,4))  #7
# print(test)   #123

# 6. можно заменить данный метод на см в init
# from my_package.module_2 import #или через init обращаться к пакету
# from my_package.module_1 import #или через init обращаться к пакету

#тут у меня не скачалась колорама и я создала новый проект
# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

#pip freeze чтобы узнать список зависимостей
# pip freeze -> requrements.txt


from faker import Faker
fake = Faker()
print(f'Name: {fake.name()}')
print(f'Address: {fake.address()}')
print(f'Tel: {fake.phone_number()}')
print(f'Email: {fake.email()}')



