from .db import mydb

def getIsland():
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM Ile")
    return cur.fetchall()

def addIsland(islandName, idIsland):
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT id_ile FROM Ile WHERE nom_ile = %s AND id_compte = %s", (islandName, idIsland))
    if cur.fetchone():
        return False
    cur.execute("INSERT INTO Ile (nom_ile, id_compte, note) VALUES (%s, %s, 0)", (islandName, idIsland))
    mydb.commit()
    return True

def getAllIslandInformations(islandName):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Ile WHERE id_ile = %s", (islandName))
    return cursor.fetchone() # only one line