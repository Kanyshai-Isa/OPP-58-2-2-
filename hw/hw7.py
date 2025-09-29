import sqlite3

connect = sqlite3.connect('my_database.db')

cursor = connect.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
id INTEGER PRIMARY KEY AUTOINCREMENT,
first_name VARCHAR (100) NOT NULL,
last_name VARCHAR (100) NOT NULL,
grade INTEGER NOT NULL,
subject TEXT
)
''')

connect.commit()

def add_student(first_name, last_name, grade, subject):
    cursor.execute(
        "INSERT INTO students(first_name, last_name, grade, subject) VALUES (?, ?, ?, ?)",
        (first_name, last_name, grade, subject)
    )
    connect.commit()
    print('Пользователь добавлен')

# add_student('Alibek', 'Kerimov', 4, 'Math')
# add_student('Sobira', 'Rakhatova', 10, 'Physics')
# add_student('Uluk', 'Batyrbekov', '1', 'Physical training')





def get_students():
    cursor.execute('SELECT first_name, last_name, grade, subject FROM students')
    students = cursor.fetchall()
    for student in students:
        print(f'first_name: {student[0]}, last_name: {student[1]}, grade: {student[2]}, subject: {student[3]}')

# get_students()





def update_user(id, first_name=None, last_name=None, grade=None, subject=None ):
    if first_name:
        cursor.execute(
            'UPDATE students SET first_name = ? WHERE id = ?',
            (first_name, id)
        )
    elif last_name:
        cursor.execute(
            'UPDATE students SET last_name = ? WHERE id = ?',
            (last_name, id)
        )
    elif grade:
        cursor.execute(
            'UPDATE students SET grade = ? WHERE id = ?',
            (grade, id)
        )
    elif subject:
        cursor.execute(
            'UPDATE students SET subject = ? WHERE id = ?',
            (subject, id)
        )
    else:
        print('Ничего не передано')
connect.commit()
print('Пользователь обновлен!!!')

update_user(3, 'Aktan')
# get_students()




def delete_student(id):
    cursor.execute(f'DELETE FROM students WHERE id = "{id}"')
    connect.commit()
    print('Пользователь удален!')

delete_student(1)

