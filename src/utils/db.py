import mysql.connector

conn = None
cursor = None


def executeTransaction(queries: list[str]):
    cursor = conn.cursor()
    try:
        for query in queries:
            cursor.execute(query)
        conn.commit()
        print("Transaction ok")
    except Exception:
        print("Transaction not ok")
    finally:
        cursor.close()


def executeSelect(query: str) -> list:
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        print("Transaction ok")
        return cursor.fetchall()
    except Exception:
        print("Transaction not ok")
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
conn.autocommit = False
