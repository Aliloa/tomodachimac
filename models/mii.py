from .db import mydb

def getAllUserMiis(idCompte):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM Mii WHERE id_compte = %s", (idCompte, ))
    return cursor.fetchall() # returns array of dictionaries containing all rows of the result

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

def getMiiCrush(idMii):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT Copy.* FROM Mii Original JOIN Mii Copy ON Original.id_crush = Copy.id_mii WHERE Original.id_mii = %s", (idMii, ))
    return cursor.fetchone()