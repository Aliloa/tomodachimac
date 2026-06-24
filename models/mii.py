from .db import mydb

def getAllUserIslandMiis(idIsland):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT nom_mii, image FROM Mii WHERE id_ile = %s", (idIsland, ))
    return cursor.fetchall() # returns array of dictionaries containing all rows of the result

def CountAllIslandMiis(idIsland): # number of miis on an island
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) as nbMiis FROM Mii WHERE id_ile = %s", (idIsland, ))
    result = cursor.fetchone() # dictionnary {"nbMiis" : number of miis on the island}
    return result["nbMiis"]

# for a single mii :
def getAllMiiInformations(idMii):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Mii WHERE id_mii = %s", (idMii, ))
    return cursor.fetchone() # only one line

def getMiiParents(idMii): 
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT id_pere, id_mere FROM Mii WHERE id_mii = %s", (idMii, ))
    return cursor.fetchone() # only one line

def getMiiSiblings(idMii):
    parents = getMiiParents(idMii) # getting mii's parents to deduce their siblings : if they have a parent in commun
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT id_mii FROM Mii WHERE (id_pere = %s OR id_mere = %s) AND id_mii != %s", (parents['id_pere'], parents['id_mere'], idMii))
    return cursor.fetchall()

def getMiiCrushInformations(idMii):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT Copy.* FROM Mii Original JOIN Mii Copy ON Original.id_crush = Copy.id_mii WHERE Original.id_mii = %s", (idMii, ))
    return cursor.fetchone()

def createMii(name, sex, age, personnality, image, idUser, idIsland):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("INSERT INTO Mii (nom_mii, sexe, age, personnalite, image) VALUES (%s, %s, %s, %s,) JOIN Ile ON Mii.id_ile = Ile.id_ile JOIN Compte ON Ile.id_compte = Compte.id_compte WHERE id_ile = %s AND id_compte = %s", (name, sex, age, personnality, image, idIsland, idUser))
    mydb.commit()