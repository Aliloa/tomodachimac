from .db import mydb

def getAllFamilyMembers(idFamily):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM mii JOIN famille ON mii.id_famille = famille.id_famille WHERE famille.id_famille = %s", (idFamily, ))
    return cursor.fetchall()

def countFamilyMembers(idFamily):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT COUNT(*) as nbMembers FROM mii JOIN famille ON mii.id_famille = famille.id_famille WHERE famille.id_famille = %s", (idFamily, ))
    return cursor.fetchone()["nbMembers"]

def getFamilyName(idFamily):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT nom_famille FROM famille WHERE id_famille = %s", (idFamily, ))
    result = cursor.fetchone()
    if result: 
        return result['nom_famille']
    else:
        return None

def getFamiliesByIsland(idIsland):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("SELECT * FROM famille JOIN mii ON mii.id_famille = famille.id_famille WHERE mii.id_ile = %s", (idIsland,))
    return cursor.fetchall()

def createFamily(familyName):
    cursor = mydb.cursor(dictionary=True)

    cursor.execute("INSERT INTO famille (nom_famille) VALUES (%s)", (familyName, ))
    mydb.commit()

    new_id = cursor.lastrowid # reading last generated id_famille
    cursor.close()
    return new_id