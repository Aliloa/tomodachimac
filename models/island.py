from .db import mydb

def getIslandsByUser(id_compte):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ile WHERE id_compte = %s", (id_compte,))
    return cursor.fetchall() 

def addIsland(islandName, idIsland):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO ile (nom_ile, id_compte, note) VALUES (%s, %s, 0)", (islandName, idIsland))
    mydb.commit()
    mycursor.close()