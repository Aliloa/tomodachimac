from .db import mydb

def getAllFamilyMembers(idFamily):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT nom_mii, image FROM mii JOIN famille ON mii.id_famille = famille.id_famille WHERE id_famille = %s", (idFamily, ))
    return cursor.fetchall()

def countFamilyMembers(idFamily):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) FROM mii JOIN famille ON mii.id_famille = famille.id_famille WHERE id_famille = %s", (idFamily, ))
    return cursor.fetchall()

def getFamilyName(idFamily):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT nom_famille FROM famille WHERE id_famille = %s", (idFamily, ))
    result = cursor.fetchall()
    if result: 
        return result['nom_famille']
    else:
        return None

def getFamiliesByIsland(idIsland):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM famille JOIN mii ON mii.id_famille = famille.id_famille WHERE mii.id_ile = %s", (idIsland,))
    return cursor.fetchall()