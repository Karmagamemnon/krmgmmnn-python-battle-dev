import mysql.connector

conn = None
cursor = None


def execute(query):
    cursor = conn.cursor()
    try:
        affected_count = cursor.execute(query, multi=True)
        conn.commit()
        print(affected_count)
        print("inserted values")
    except Exception:
        print("failed to insert values")
    finally:
        cursor.close()


def count(query):
    cursor = conn.cursor()
    cursor.execute(query)
    count = cursor.fetchone()[0]
    cursor.close()
    return count


def closeConnection():
    conn.close()


conn = mysql.connector.connect(
    host="localhost", user="python", password="python123", database="pythonbattledev_db")
