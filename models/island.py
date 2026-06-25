from .db import mydb

def getAllIslands():
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM ile")
    return mycursor.fetchall() 

def getIslandsByUser(id_compte):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM ile WHERE id_compte = %s", (id_compte,))
    return mycursor.fetchall() 

def getIslandById(id_island):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM ile WHERE id_ile = %s", (id_island,))
    return mycursor.fetchone() 

def addIsland(islandName, idIsland):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO ile (nom_ile, id_compte, note) VALUES (%s, %s, 0)", (islandName, idIsland))
    mydb.commit()
    mycursor.close()

def deleteIslandById(id_island):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM ile WHERE id_ile = %s", (id_island,))
    mydb.commit()
    mycursor.close()