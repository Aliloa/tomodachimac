from .db import mydb

def getIsland():
    cur = mydb.cursor(dictionary=True)
    cur.execute("SELECT * FROM Ile")
    return cur.fetchall()

def addIsland(islandName, idIsland):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO Ile (nom_ile, id_compte, note) VALUES (%s, %s, 0)", (islandName, idIsland))
    mydb.commit()
    mycursor.close()

def getAllIslandInformations(islandName):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Ile WHERE id_ile = %s", (islandName))
    return cursor.fetchone() # only one line