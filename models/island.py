from .db import mydb

def getIsland():
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM ile")
    return cur.fetchall()
