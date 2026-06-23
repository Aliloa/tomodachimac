import mysql.connector

def initDb():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="tomodachimac"
    )

#recup données
def getData():
    print('---------------------')
    mydb = initDb()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''select * from users''')
    result = mycursor.fetchall()
    return result

#ajouter données
def inputData(nom):
    mydb = initDb()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO users (nom) VALUES (%s)", (nom,))
    mydb.commit()
    mycursor.close()

#maj données

#supprimer données
def deleteData(delete_id):
    mydb = initDb()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM users WHERE id = %s", (delete_id,))
    mydb.commit()
    mycursor.close()

def connexion(pseudo, mdp):
    mydb = initDb()
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM users WHERE pseudo = %s AND mdp = %s", (pseudo, mdp))
    return mycursor.fetchone()  # renvoie l'user si trouvé, None sinon