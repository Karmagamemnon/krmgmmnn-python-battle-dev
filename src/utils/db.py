import mysql.connector

conn = None
cursor = None


def execute(query):
    cursor.execute(query)
    conn.commit()


def count(query):
    cursor.execute(query)
    count = cursor.fetchone()[0]
    return count


def closeConnection():
    conn.close()


conn = mysql.connector.connect(
    host="localhost", user="python", password="python123", database="pythonbattledev_db")
cursor = conn.cursor()
