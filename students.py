import sqlite3

def init_db():
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fio TEXT UNIQUE NOT NULL,
               speciality TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()


def insert_user(fio, speciality):
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        cursor.execute ('''INSERT INTO students (fio, speciality) 
                        VALUES (?,?)''',(fio, speciality))

        conn.commit()
        conn.close()

def update_user(id, fio, speciality):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE students SET fio = ?, speciality = ?
        WHERE id = ?
    ''', (fio, speciality, id))
    conn.commit()
    conn.close() 
        
def delete_user(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor() 
    cursor.execute('DELETE FROM pethome WHERE id = ?', (id,))
    conn.commit()
    conn.close()

def get_user_by_id(id):
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM students WHERE id = ?', (id,))
    user = cursor.fetchone()  
    conn.close()
    return user

if __name__ == '__main__':
    init_db()
    
    while True:
        enter = input("Введите функцию для выполнения (update,delete,insert,get_user_by_id,break): ")

        if enter == "update":

            id = int(input("Введите id для обновления: "))
            fio = input("Введите новое ФИО: ")
            speciality = input("Введите новую специальность: ")
            update_user(id, fio, speciality)

        elif enter == "delete":

            id = int(input("Введите id для удаления: "))
            delete_user(id)

        elif enter == "insert":

            fio = input("Введите ФИО: ")
            speciality = input("Введите специальность: ")
            insert_user(fio, speciality)

        elif enter == "get_user_by_id":

            id = int(input("Введите id студента: "))
            user_data = get_user_by_id(id)
            if user_data:
                print("Данные студента:")
                print(f"ID: {user_data[0]}")
                print(f"ФИО: {user_data[1]}")
                print(f"Специальность: {user_data[2]}")
            else:
                print(f"Студент с таким ID {id} не найден.")
        elif enter == "break":
            print("Работа программы завершена.")
            break

        else:
            print("Некорректный ввод. Повторите.")