from .db import mydb

def getAllUserIslandMiis(idUser, idIsland):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM mii JOIN ile ON mii.id_ile = ile.id_ile JOIN compte ON compte.id_compte = ile.id_compte WHERE (mii.id_ile = %s AND ile.id_compte = %s )", (idIsland, idUser))
    return cursor.fetchall() # returns array of dictionaries containing all rows of the result

def CountAllIslandMiis(idIsland): # number of miis on an island
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) as nbMiis FROM mii WHERE id_ile = %s", (idIsland, ))
    result = cursor.fetchone() # dictionnary {"nbMiis" : number of miis on the island}
    return result["nbMiis"]

# for a single mii :
def getAllMiiInformations(idMii):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM mii WHERE id_mii = %s", (idMii, ))
    return cursor.fetchone() # only one line

def getMiiParents(idMii): 
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT id_pere, id_mere FROM mii WHERE id_mii = %s", (idMii, ))
    return cursor.fetchone() # only one line

def getMiiSiblings(idMii):
    parents = getMiiParents(idMii) # getting mii's parents to deduce their siblings : if they have a parent in commun
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT id_mii FROM mii WHERE (id_pere = %s OR id_mere = %s) AND id_mii != %s", (parents['id_pere'], parents['id_mere'], idMii))
    return cursor.fetchall()

def getMiiCrushInformations(idMii):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT Copy.* FROM mii Original JOIN mii Copy ON Original.id_crush = Copy.id_mii WHERE Original.id_mii = %s", (idMii, ))
    return cursor.fetchone()

def getMiiPartnerInformations(idMii):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT Copy.* FROM mii Original JOIN mii Copy ON Original.id_partenaire = Copy.id_mii WHERE Original.id_mii = %s", (idMii, ))
    return cursor.fetchone()

def createMii(name, sex, age, personnality, image, idUser, idIsland):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("INSERT INTO mii (nom_mii, sexe, age, personnalite, image, id_ile) VALUES (%s, %s, %s, %s, %s, %s)", (name, sex, age, personnality, image, idIsland))
    mydb.commit()