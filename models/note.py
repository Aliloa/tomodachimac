from .db import mydb

def getNote():
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM note")
    return cur.fetchall()
