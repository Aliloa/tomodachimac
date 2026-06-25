from .db import mydb

def getAllIslands():
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ile")
    return cursor.fetchall() 

def getIslandsByUser(id_compte):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ile WHERE id_compte = %s", (id_compte,))
    return cursor.fetchall() 

def getIslandById(id_island):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ile WHERE id_ile = %s", (id_island,))
    return cursor.fetchone() 

def addIsland(islandName, idIsland):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO ile (nom_ile, id_compte, note) VALUES (%s, %s, 0)", (islandName, idIsland))
    mydb.commit()
    mycursor.close()