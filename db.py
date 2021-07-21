import mysql.connector

conn = None
cursor = None

def saveSample(sample):
    #Check if sample doesn't exist
    cursor.execute("SELECT count(*) FROM sample WHERE id = %s", sample.id)

    result = cursor.fetchall()
    print(result)

def closeConnection():
    conn.close()


conn = mysql.connector.connect(host="192.168.1.89", user="python", password="python123", database="pythonbattledev_db")
cursor = conn.cursor()
