import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'M@103!z2'
)

myCursor = dataBase.cursor()

myCursor.execute("CREATE DATABASE userdb")

print("Done")