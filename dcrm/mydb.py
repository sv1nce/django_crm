import pymysql

# Параметри підключення до бази даних
db_params = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
}

# Підключення до сервера бази даних
connection = pymysql.connect(**db_params)

# Створення курсора
cursor = connection.cursor()

# Створення бази даних
database_name = 'romkacorp'
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

# Закриття курсора та підключення
cursor.close()
connection.close()

print('All Done')
