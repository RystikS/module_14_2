import sqlite3


connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
"""Заполнение таблицы данными"""
# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}gmail.com', f'{i*10}', 1000))

"""Обновление баланса"""
# for i in range(1, 11, 2):
# cursor.execute(f'UPDATE Users SET balance = ? WHERE id = {i}', (500, ) )

"""Удаление информации"""
# for i in range(1, 11, 3):
#     cursor.execute(f'DELETE FROM Users WHERE id = {i}')

"""Выборка всех записей при помощи fetchall()"""
# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60', )
# users = cursor.fetchall()
#
# for user in users:
#     username, email, age, balance = user
#     print( f'Имя: {username} | Почта: {email} | Возраст: {age} | Баланс: {balance}')


"""Удаление информации из базы данных not_telegram"""
cursor.execute('DELETE FROM Users WHERE id = 6')
"""Подсчет общего количества записей"""
cursor.execute('SELECT COUNT(id) FROM Users')
total_users = cursor.fetchone()[0]
"""Подсчет суммы всех балансов"""
cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
"""Вывод среднего баланса всех пользователей в консоль"""
print(total_balance/total_users)


connection.commit()
connection.close()