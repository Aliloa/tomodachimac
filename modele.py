import mysql.connector
# for .env : 
import os
from dotenv import load_dotenv

load_dotenv()

# informations of the database depend on local .env
mydb = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
)

#recup données
def getData():
    print('---------------------')
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute('''select * from users''')
    result = mycursor.fetchall()
    return result

#ajouter données
def inputData(nom):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("INSERT INTO users (nom) VALUES (%s)", (nom,))
    mydb.commit()
    mycursor.close()

#maj données

#supprimer données
def deleteData(delete_id):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("DELETE FROM users WHERE id = %s", (delete_id,))
    mydb.commit()
    mycursor.close()

def connexion(pseudo, mdp):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM users WHERE pseudo = %s AND mdp = %s", (pseudo, mdp))
    return mycursor.fetchone()  # renvoie l'user si trouvé, None sinon