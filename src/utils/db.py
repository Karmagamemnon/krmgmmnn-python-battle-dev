import mysql.connector

conn = None
cursor = None


def execute(query):
    cursor.execute(query, multi=True)
    conn.commit()
    print(f"Transaction ok")


def count(query):
    cursor.execute(query)
    count = cursor.fetchone()[0]
    return count


def closeConnection():
    conn.close()


conn = mysql.connector.connect(
    host="localhost", user="python", password="python123", database="pythonbattledev_db")
cursor = conn.cursor()
