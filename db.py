import mysql.connector

conn = None
cursor = None


def saveSample(sample):
    # Check if sample doesn't exist
    cursor.execute("SELECT COUNT(1) FROM sample WHERE id = " + str(sample.id))
    count = cursor.fetchone()[0]
    print(count)
    if count == 0:
        print("Sample doesn't exist yet")
    else:
        print("Sample exists")


def closeConnection():
    conn.close()


conn = mysql.connector.connect(
    host="localhost", user="python", password="python123", database="pythonbattledev_db")
cursor = conn.cursor()
