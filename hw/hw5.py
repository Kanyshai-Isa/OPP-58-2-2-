# def check_admin(role):
#     def decorator(func):
#         def wrapper():
#             while True:
#                 role = input('Введите роль: ')
#                 if role == 'админ':
#                     func()
#                 else:
#                     print('Доступ запрещен')
#                     pass
#         return wrapper
#     return decorator
#
# @check_admin('админ' or 'арзы')
# def delete_user():
#     print('Пользователь удалён')
#
# @check_admin('админ' or 'арзы')
# def add_user():
#     print('Пользователь добавлен')


# delete_user()
# add_user()


class User:
    def __init__(self, login, role):
        self.login = login
        self.role = role

def check_user_admin(User):
    def decorator(func):
        def wrapper():
            if User.role == "админ":
                return func()
            else:
                return print(f'Доступ запрещен для "{User.role}"')
        return wrapper
    return decorator

admin = User("Temirlan", "админ")
guest = User("Ardager", "пользователь")

@check_user_admin(admin)
def create_report():
   print("Отчёт создан")


@check_user_admin(guest)
def delete_report():
   print("Отчёт удалён")


create_report()
delete_report()