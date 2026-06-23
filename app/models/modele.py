import mysql.connector

def initDb():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="test"
    )

#recup données
def getData():
    print('---------------------')
    mydb = initDb()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''select * from etudiants''')
    result = mycursor.fetchall()
    return result

#ajouter données
def inputData(nom):
    mydb = initDb()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO etudiants (nom) VALUES (%s)", (nom,))
    mydb.commit()
    mycursor.close()

#maj données

#supprimer données
def deleteData(delete_id):
    mydb = initDb()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM etudiants WHERE id = %s", (delete_id,))
    mydb.commit()
    mycursor.close()
