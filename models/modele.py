import mysql.connector

mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tomodachimac"
)

#recup données
def getData():
    print('---------------------')
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''select * from etudiants''')
    result = mycursor.fetchall()
    return result

#ajouter données
def inputData(nom):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO etudiants (nom) VALUES (%s)", (nom,))
    mydb.commit()
    mycursor.close()

#maj données

#supprimer données
def deleteData(delete_id):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM etudiants WHERE id = %s", (delete_id,))
    mydb.commit()
    mycursor.close()