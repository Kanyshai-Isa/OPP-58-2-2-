import sqlite3

#a4
connect = sqlite3.connect('users.db')   #или con

#рука с ручкой
cursor = connect.cursor()   #connect как объект


cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
name VARCHAR (100) NOT NULL,
age INTEGER NOT NULL,
hobby TEXT
)
''')

connect.commit()

# CRUD = create - read - update - delete

def add_user(name_1, age, hobby):
    # cursor.execute(f'INSERT INTO users(name, age, hobby) VALUES ("{name}", "{age}", "{hobby}")') это незащищенный подход
    cursor.execute(
        "INSERT INTO users(name, age, hobby) VALUES (?, ?, ?)",
        (name_1, age, hobby)
    )
    connect.commit()
    print('Пользователь добавлен')

# add_user('Ardager', 26, 'Спать!!')
# add_user('Oleg', 33, 'Храпеть')

def get_users():
    cursor.execute('SELECT name, age, hobby FROM users')   #*-все столбцы CtrlA
    users = cursor.fetchall()
    # users = cursor.fetchone()
    # users = cursor.fetchmany(2)
    for user in users:
        print(f'name: {user[0]}, age: {user[1]}, hobby: {user[2]}')

# get_users()

def update_user(row_id, name=None, age=None, hobby=None ):
    if name:
        cursor.execute(
            'UPDATE users SET name = ? WHERE rowid = ?',
            (name, row_id)
        )
    elif age:
        cursor.execute(
            'UPDATE users SET age = ? WHERE rowid = ?',
            (age, row_id)
        )
    elif hobby:
        cursor.execute(
            'UPDATE users SET hobby = ? WHERE rowid = ?',
            (hobby, row_id)
        )
    else:
        print('Ничего не передано')
    connect.commit()
    print('Пользователь обнавлен!!!')

update_user("Arzybek", 2)
update_user('45', 3)
get_users()