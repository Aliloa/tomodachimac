from .db import mydb

def getMiis():
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM mii")
    return cur.fetchall()