from .db import mydb

def getIsland():
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM Ile")
    return cur.fetchall()

def getAllIslandInformations(idIsland):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Ile WHERE id_ile = %s", (idIsland, ))
    return cursor.fetchone() # only one line