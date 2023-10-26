import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password'
)

#prepare cursor object
cursorObject = dataBase.cursor()

#creating database
cursorObject.execute('CREATE DATABASE romkacorp')

print('All Done')